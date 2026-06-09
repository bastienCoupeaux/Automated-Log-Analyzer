# ------------------------------------------------------
# --- Cybersecurity project : Automated log analyzer ---
# ------------------------------------------------------

# Author : Bastien Coupeaux 
# Date : 09/06/2026

# -----------------
# --- Libraries ---
# -----------------

import re
import sys
from tkinter import Tk, filedialog
from collections import Counter

# ------------------------
# --- Global variables ---
# ------------------------

# Pattern to look for in the log file 
LogsPattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*"\s(\d{1,3})'

# -----------------
# --- Functions ---
# -----------------

def openFile() : # Ask the user which file he wants to open

    # Input : Nothing 
    # Output : The path to the file the user wants to open

    # Create the main window
    root = Tk()

    # Hide it, we juste want to see the window to select the file
    root.withdraw()
    root.attributes('-topmost',True)

    # Open the window to ask the user which file he want to select 
    pathToFile = filedialog.askopenfilename(title='Select the log file.', filetypes=[('Text files','*.txt'), ('Log files','*.log')])

    # Close the window 
    root.destroy()

    if pathToFile : 
        return pathToFile
    else : 
        print("Error! You haven't selected any files?")
        sys.exit()

def logAnalysis(pathToFile) : 

    # Initialize the 404 error and IP address dictionaries
    ipAdress = Counter()
    error404 = Counter()

    try : 
        with open(pathToFile,'r',encoding='utf-8') as file : 
            for row in file : 

                # We search the pattern in each row of the file 
                match = re.search(LogsPattern,row)

                # If we find the pattern, we collect the information
                if match : 

                    # Collect the IP (group 1) and the error type (group 2)
                    ip = match.group(1)
                    errorType = match.group(2)

                    # We add the ip to its dictionnary
                    ipAdress[ip] +=1

                    # If the errorType = 404, we keep the information. If not, we don't care.
                    if errorType == '404' : 

                        # Add to the dictionnary
                        error404[ip] +=1
            
            # Show the results
            print('Top IP Addresses')
            for ip, number in ipAdress.most_common() : 
                print(f"IP adress : {ip} -> {number} requests.")

            print("Scan attempts / Pages not found")
            for ip, number in error404.items() : 
                if number>=1 : 
                    print(f"The IP address: {ip} has generated {number} 404 errors. Suspected vulnerability scan! ")

    except FileNotFoundError:
        print(f"[ERROR] The file {pathToFile} was not found. Create it first !")

# ------------------------
# --- Body of the code ---
# ------------------------

if __name__ == '__main__':
    # Get the file path
    chosenFile = openFile()
    
    # Process the analysis
    logAnalysis(chosenFile)



