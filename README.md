# auto-recon-tool
Auto recon tool using Python – Runs Nmap, Gobuster, Whois, and Dig – Output saved in folders

**This project is intended for educational use only.**

---

# Disclaimer

> This tool is created for **learning and educational purposes only**.  
> Unauthorized scanning or access to systems you don't own is **strictly prohibited**.  
> The author is **not responsible** for any misuse.

---

# Folder Structure

auto-recon-tool/
├── recon.py
├── requirements.txt     # This file lists Python dependencies. External tools (e.g., gobuster, whois) must be installed manually.
├── wordlists/           # Place downloaded wordlists from requirements.txt in here
├── results/             # Auto-generated scan results
├── .gitignore
├── LICENSE
└── README.md

# Features

- Automated scanning workflow
- Runs:
  - Nmap (Port scanning)
  - Gobuster (Directory brute-forcing)
  - Whois (Domain lookup)
  - Dig (DNS queries)
- Creates timestamped folders for organized results

---

# Requirements

# Python modules (install via pip)
