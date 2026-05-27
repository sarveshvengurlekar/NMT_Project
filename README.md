# NMT_Project

A collection of Python-based network monitoring and packet analysis projects.

## 📋 Table of Contents

- [About](#about)
- [Projects](#projects)
  - [Project 1: Network Uptime Monitor](#project-1-network-uptime-monitor)
  - [Project 2: Packet Sniffer & Analyzer](#project-2-packet-sniffer--analyzer)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## 📖 About

This repository contains a collection of network monitoring and packet analysis tools written in Python. These projects demonstrate practical network utilities for system monitoring, network diagnostics, and packet inspection.

**Language:** Python 100%

## 🎯 Projects

### Project 1: Network Uptime Monitor

A system monitoring tool that tracks the uptime of a target host and calculates Service Level Agreement (SLA) metrics.

**Features:**
- Continuous ping monitoring of target host
- System uptime tracking
- Downtime event logging
- Real-time SLA calculation
- Timestamped event logging

**Key Files:**
- `Proj_1/code.py` - Main monitoring script
- `Proj_1/uptime_log.txt` - Log file for monitoring events

**Target:** Monitors Google DNS (8.8.8.8) with 10-second check intervals

### Project 2: Packet Sniffer & Analyzer

A network packet capture and analysis tool using Scapy for real-time packet inspection.

**Features:**
- Real-time packet capture and analysis
- Layer 3 (IP) protocol identification
- Layer 4 (TCP, UDP, ICMP) protocol detection
- Source and destination IP extraction
- Formatted packet information display

**Key Files:**
- `Proj_2/test_code.py` - Packet sniffing and analysis script
- `Proj_2/alert.log` - Alert log file

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/sarveshvengurlekar/NMT_Project.git
cd NMT_Project
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install psutil scapy
```

## 💻 Usage

### Project 1: Network Uptime Monitor

Run the uptime monitoring tool:
```bash
cd Proj_1
python code.py
```

The script will:
- Begin monitoring the target host (8.8.8.8)
- Log each ping result with timestamp
- Calculate and display SLA percentage
- Continue running indefinitely (press Ctrl+C to stop)

Logs are saved to `Proj_1/uptime_log.txt`

### Project 2: Packet Sniffer & Analyzer

Run the packet sniffer:
```bash
cd Proj_2
python test_code.py
```

The script will:
- Start capturing network packets
- Display packet information including:
  - Packet number
  - Source IP address
  - Destination IP address
  - Protocol type (TCP, UDP, ICMP, or Other)
- Continue capturing until stopped (press Ctrl+C to stop)

**Note:** May require administrator/root privileges to capture packets.

## 📁 Project Structure

```
NMT_Project/
├── README.md
├── Proj_1/
│   ├── code.py                 # Network uptime monitor
│   └── uptime_log.txt          # Uptime monitoring logs
└── Proj_2/
    ├── test_code.py            # Packet sniffer & analyzer
    └── alert.log               # Alert logs
```

## 🔧 Dependencies

- **psutil** - For system and process utilities (used in Proj_1)
- **scapy** - For packet manipulation and analysis (used in Proj_2)

Install with:
```bash
pip install psutil scapy
```

## 📝 Notes

- Packet sniffing in Project 2 requires elevated privileges (admin/root)
- The uptime monitor in Project 1 uses 10-second intervals between checks
- SLA calculations in Project 1 are based on ping success rate
- Both projects use continuous loops and require manual interruption (Ctrl+C) to stop

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add improvement'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Last Updated:** May 27, 2026
