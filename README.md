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
- recon.py
- wordlists/           # Place downloaded wordlists from requirements.txt in here
- results/             # Auto-generated scan results
- requirements.txt     # This file lists Python dependencies. External tools (e.g., gobuster, whois) must be installed manually.
- .gitignore
- LICENSE
- README.md

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

Python Modules (install via pip) 
dnspython       # For DNS resolution in recon.py

External Tools (install or download manually)
Gobuster (Windows binary): https://github.com/OJ/gobuster/releases
Whois (Windows binary): https://docs.microsoft.com/en-us/sysinternals/downloads/whois

Wordlists (download manually)
Recommended:
- directory-list-2.3-medium.txt
- directory-list-2.3-small.txt
- raft-small-words.txt
- common.txt
Download from: https://github.com/danielmiessler/SecLists
Place all wordlists into a folder named `wordlists/`

---

# Possible Improvements

- Add more recon tools such as RustScan, Masscan, or Subfinder for wider coverage
- Export results to HTML or JSON format for better report sharing
- Add looped or scheduled scans for continuous monitoring of a target
- Integrate public APIs like Shodan, Censys, or VirusTotal for enriched intelligence
- Enable threading or multiprocessing to speed up large-scale scans
- Develop a lightweight GUI with Tkinter or web UI for user-friendly operation

---

# Use Cases

- Learning scripting + tool integration for beginners in cybersecurity
- Practicing reconnaissance in CTFs or lab environments
- Serving as a building block for a larger red-team or automation toolkit
- Teaching automation workflows in cybersecurity or ethical hacking courses
- Quick recon on internal test environments without relying on manual steps

