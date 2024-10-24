# Port Scanner Script

## Overview
This project provides a **Python-based Port Scanner** that allows you to scan an IP address and determine which ports are open and closed. The tool is capable of scanning the entire range of ports (1-65535) and provides detailed descriptions of each port.

The results are saved to a text file, which includes:
- A summary of the total number of open and closed ports.
- A complete list of open ports followed by a list of closed ports.
- A separator line between open and closed ports for better readability.

The `.exe` version of the script is also available for use on systems without Python installed.

## Features
- **Full Port Range Scan**: Scans all 65535 ports on a target IP address.
- **Detailed Descriptions**: Provides descriptions for well-known ports, making it easier to understand what each open port is used for.
- **Multithreaded Scanning**: Uses concurrent multithreading to significantly speed up the scanning process.
- **Comprehensive Report**: Generates a detailed report saved as a text file, with open ports listed at the top and closed ports listed below.

## Usage

### Python Version
1. **Clone the repository**:
   ```sh
   git clone <repository-url>
   cd port-scanner-script
   ```

2. **Install dependencies**:
   The script uses the Python standard library only, so no additional dependencies are needed.

3. **Run the script**:
   ```sh
   python port_scanner_script.py
   ```

4. **Enter the IP address** to scan when prompted.

5. **Check the results** in the generated text file in the current directory. The file will be named according to the IP address and the current date and time (e.g., `192.168.1.1-2024-10-25_12-30-00.txt`).

### Executable Version
If you don't have Python installed, you can use the executable version:
1. **Download the `.exe` file** from the releases section.
2. **Run the `.exe`** file directly on a Windows machine.
3. **Enter the IP address** when prompted, and the tool will generate a text file with the scan results in the same directory.

## Report Format
The generated report will contain:
- **Total Open Ports**: Count of open ports.
- **Total Closed Ports**: Count of closed ports.
- **Open Ports**: List of open ports with descriptions.
- A separator line (`************************************`)
- **Closed Ports**: List of closed ports with descriptions.

## Example
Sample report snippet:
```
Scan results for IP: 192.168.1.150
Scan date and time: 2024-10-25_12-30-00

Total open ports: 5
Total closed ports: 65530

Open Ports:
Port 22 - open (SSH - Secure Shell)
Port 80 - open (HTTP - Hypertext Transfer Protocol)
...

************************************

Closed Ports:
Port 21 - closed (FTP - File Transfer Protocol (Command))
Port 23 - closed (Telnet - Unsecure Remote Login)
...
```

## Building `.exe` from Python Script
To build an `.exe` file from the Python script, follow these steps:
1. **Install PyInstaller**:
   ```sh
   pip install pyinstaller
   ```
2. **Create the executable**:
   ```sh
   pyinstaller --onefile port_scanner_script.py
   ```
3. The resulting `.exe` will be located in the `dist` folder.

## Requirements
- Python 3.6 or higher (if running the Python version).
- Windows OS for `.exe` version.
- **No additional dependencies** for Python script—uses standard libraries only.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

## Contributions
Contributions are welcome! Feel free to fork this repository and submit pull requests.

## Disclaimer
This tool is intended for educational and authorized use only. Unauthorized scanning of networks is illegal, and the author assumes no responsibility for any misuse of this tool.
