import socket
import ipaddress
import concurrent.futures
import datetime
import os

# Function to check if a port is open
def is_port_open(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.1)  # Timeout set to 0.1 seconds for faster scanning
        result = s.connect_ex((ip, port))
        return result == 0  # If result is 0, the port is open

# Port descriptions (full list from 1 to 65535)
port_descriptions = {
    1: "TCP Port Service Multiplexer (TCPMUX)",
    5: "Remote Job Entry (RJE)",
    7: "Echo Protocol",
    18: "Message Send Protocol (MSP)",
    20: "FTP - File Transfer Protocol (Data)",
    21: "FTP - File Transfer Protocol (Command)",
    22: "SSH - Secure Shell",
    23: "Telnet - Unsecure Remote Login",
    25: "SMTP - Simple Mail Transfer Protocol",
    37: "Time Protocol",
    42: "Host Name Server (Nameserv)",
    43: "WHOIS Protocol",
    49: "TACACS+ Login Host Protocol",
    53: "DNS - Domain Name System",
    67: "DHCP - Dynamic Host Configuration Protocol (Server)",
    68: "DHCP - Dynamic Host Configuration Protocol (Client)",
    69: "TFTP - Trivial File Transfer Protocol",
    70: "Gopher Protocol",
    79: "Finger Protocol",
    80: "HTTP - Hypertext Transfer Protocol",
    110: "POP3 - Post Office Protocol",
    111: "ONC RPC (Sun RPC)",
    119: "NNTP - Network News Transfer Protocol",
    123: "NTP - Network Time Protocol",
    135: "MS RPC - Microsoft Remote Procedure Call",
    137: "NetBIOS - Name Service",
    138: "NetBIOS - Datagram Service",
    139: "NetBIOS - Session Service",
    143: "IMAP - Internet Message Access Protocol",
    161: "SNMP - Simple Network Management Protocol",
    162: "SNMPTRAP - SNMP Trap",
    179: "BGP - Border Gateway Protocol",
    194: "IRC - Internet Relay Chat",
    201: "AppleTalk Routing Maintenance",
    443: "HTTPS - Secure HTTP",
    445: "Microsoft-DS - Active Directory, Windows shares",
    465: "SMTPS - Secure SMTP",
    514: "Syslog - System Logging",
    515: "LPD - Line Printer Daemon",
    520: "RIP - Routing Information Protocol",
    521: "RIPng - Routing Information Protocol Next Generation",
    587: "SMTP - Submission",
    631: "IPP - Internet Printing Protocol",
    993: "IMAPS - Secure IMAP",
    995: "POP3S - Secure POP3",
    1080: "SOCKS - Proxy Protocol",
    1194: "OpenVPN",
    1433: "MSSQL - Microsoft SQL Server",
    1521: "Oracle - Oracle Database",
    1701: "L2TP - Layer 2 Tunneling Protocol",
    1723: "PPTP - Point-to-Point Tunneling Protocol",
    1812: "RADIUS Authentication Protocol",
    1813: "RADIUS Accounting Protocol",
    2049: "NFS - Network File System",
    2083: "HTTPS - cPanel Secure",
    3306: "MySQL Database",
    3389: "RDP - Remote Desktop Protocol",
    5432: "PostgreSQL Database",
    5900: "VNC - Virtual Network Computing",
    5985: "WinRM - Windows Remote Management (HTTP)",
    5986: "WinRM - Windows Remote Management (HTTPS)",
    6379: "Redis Database",
    8000: "Common Web Servers and Development Services",
    8080: "HTTP Proxy - Alternative HTTP",
    8443: "HTTPS - Alternative HTTPS",
    9000: "SonarQube - Code Quality and Code Security",
    9090: "OpenVPN - Web UI",
    10000: "Webmin - Web-based Server Management",
    27017: "MongoDB Database",
    50000: "SAP - Systems, Applications, and Products in Data Processing",
    50070: "Hadoop HDFS HTTP WebUI",
}

# Add description for all other ports stating that it's unknown
for port in range(1, 65536):
    if port not in port_descriptions:
        port_descriptions[port] = f"Port {port} - Description unknown"

# Request IP address
ip = input("Enter the IP address to scan: ")

try:
    # Validate IP address
    ipaddress.ip_address(ip)
except ValueError:
    print("Error: Invalid IP address.")
    exit(1)

# Create filename for saving results
current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"{ip}-{current_time}.txt"

# Lists to store open and closed ports
open_ports = []
closed_ports = []

# Function to scan port and classify its status
def scan_port(port):
    if is_port_open(ip, port):
        description = port_descriptions.get(port, "Description unknown")
        result = f"Port {port} - open ({description})"
        open_ports.append(result)
    else:
        description = port_descriptions.get(port, "Description unknown")
        result = f"Port {port} - closed ({description})"
        closed_ports.append(result)

# Use multithreading to speed up scanning
print(f"\nStarting scan for IP: {ip}...\n")
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_port, range(1, 65536))

# Write results to file
with open(filename, 'w') as file:
    file.write(f"Scan results for IP: {ip}\n")
    file.write(f"Scan date and time: {current_time}\n\n")
    file.write(f"Total open ports: {len(open_ports)}\n")
    file.write(f"Total closed ports: {len(closed_ports)}\n\n")
    
    file.write("Open Ports:\n")
    for open_port in open_ports:
        file.write(open_port + "\n")
    
    file.write("\n************************************\n\n")
    
    file.write("Closed Ports:\n")
    for closed_port in closed_ports:
        file.write(closed_port + "\n")

print("\nScan completed.")
