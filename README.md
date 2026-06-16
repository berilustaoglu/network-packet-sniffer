# 🌐 Lightweight Network Packet Sniffer

A Python-based passive network monitoring tool designed to capture, parse, and display real-time network traffic (IP packets, TCP/UDP protocols) passing through the local network interface.

## ⚙️ How It Works
- **Packet Ingestion:** Uses raw socket monitoring via the **Scapy** library to sniff incoming and outgoing network data frames.
- **Protocol Dissection:** Filters and extracts core network layers such as the **IPv4 Layer**, separating source IPs, destination IPs, and transport layer protocols (TCP/UDP).
- **Security Auditing:** Helps security analysts inspect unexpected outbound connections or potential data exfiltration vectors.

## 🚀 Features
- **Real-Time Traffic Analysis:** Live-streamed terminal dashboard tracking network activity.
- **Protocol Classification:** Instantly identifies packet encapsulation types (TCP, UDP).
- **Lightweight Architecture:** Zero performance overhead on the host network interface.

## 💻 Prerequisites & Usage

1. Install the required network engineering library:
```bash
pip install scapy
```

2. Run the tool with administrative privileges (Required for raw socket access):
- **Windows (CMD/PowerShell):** Run as Administrator and execute `python sniffer.py`
- **Linux/Mac:** Run `sudo python3 sniffer.py`
