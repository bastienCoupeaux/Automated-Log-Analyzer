# Automated Log Analyzer

A lightweight Python CLI tool designed for cybersecurity beginners and system administrators to parse web server logs, detect anomalies, and flag potential vulnerability scans (e.g., high frequency of 404 errors).

## Features
* **Interactive File Selection:** Built-in GUI file explorer using Tkinter to easily select logs on your OS.
* **Regex-Powered Parsing:** High-performance extraction of IP addresses and HTTP status codes.
* **Security Auditing:** Automatically flags IP addresses acting suspiciously (e.g., directory busting, automated vulnerability probing).

## Installation & Usage
1. Clone the repository :
   ```bash
   git clone [https://github.com/bastienCoupeaux/Automated-Log-Analyzer.git](https://github.com/bastienCoupeaux/Automated-Log-Analyzer.git)
   cd Automated-Log-Analyzer

2. Run the script :
   ```bash
   python AutomatedLogAnalyzer.py
