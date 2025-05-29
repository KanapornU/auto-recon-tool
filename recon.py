'''
ทดสอบ code ใน terminal "python recon.py example.com"
wordlist หนึ่งในหัวใจของเครื่องมือ Gobuster, Dirb, Hydra, และอีกหลายตัวในสาย penetration testing

Auto Recon Tool
ผู้ใช้ป้อน target (IP/Domain) ผ่าน command line
โปรแกรมจะรัน nmap, gobuster, whois, และ dig จากนั้นเก็บผลลัพธ์ลงโฟลเดอร์
'''

import sys                      # ใช้รับค่า argument จาก command line
import os                       # ใช้จัดการโฟลเดอร์/ไฟล์
import subprocess               # ใช้รันคำสั่ง Linux (เช่น nmap, gobuster)
import dns.resolver
from datetime import datetime   # ใช้ตั้งชื่อโฟลเดอร์ด้วย timestamp

# ---------- Function: สร้างโฟลเดอร์เก็บผลลัพธ์ ----------
def create_output_dir(target):
    now = datetime.now().strftime("%Y%m%d_%H%M%S")  # สร้าง timestamp เช่น 20240528_1420
    path = f"results/{target}_{now}"                # ชื่อโฟลเดอร์รวม target และเวลา
    try:
        os.makedirs(path, exist_ok=True)            # สร้างโฟลเดอร์ (ถ้ายังไม่มี)
    except Exception as e:
        print(f"[!] Failed to create output directory: {e}")
        sys.exit(1)
    return path

# ---------- Function: รันคำสั่งแล้วเขียนผลลัพธ์ลงไฟล์ ----------
def run_command(command, output_file):
    try:
        with open(output_file, "w") as f:           # สร้างไฟล์ผลลัพธ์
            subprocess.run(command, stdout=f, stderr=subprocess.STDOUT, text=True, check=False)
    except Exception as e:
        print(f"[!] Error running command: {' '.join(command)}\n{e}")

# ---------- Function: Nmap ----------
def nmap_scan(target, path):
    print("[+] Running Nmap...")
    command = ["nmap", "-sC", "-sV", target]
    output = f"{path}/nmap.txt"
    run_command(command, output)

# ---------- Function: Gobuster ----------
def gobuster_scan(target, path):
    print("[+] Running Gobuster...")
    url = f"http://{target}"
    wordlist = "D:/GitHub/auto-recon-tool/wordlists/common.txt"
    output = f"{path}/gobuster.txt"
    command = ["D:/GitHub/auto-recon-tool/gobuster.exe/gobuster", "dir", "-u", url, "-w", wordlist]
    run_command(command, output)

# ---------- Function: WHOIS ----------
def whois_lookup(target, path):
    print("[+] Running WHOIS...")
    output = f"{path}/whois.txt"
    whois_path = "D:/GitHub/auto-recon-tool/whois64.exe"  # path แบบถูกต้อง

    try:
        result = subprocess.run([whois_path, target], capture_output=True, text=True)
        with open(output, "w", encoding="utf-8") as f:
            f.write(result.stdout)
    except Exception as e:
        print(f"[!] WHOIS lookup failed: {e}")

# ---------- Function: DIG ----------
def dig_lookup(target, path):
    print("[+] Running DNS lookup (using dnspython)...")
    output = f"{path}/dig.txt"
    try:
        result = dns.resolver.resolve(target, 'A')  # A = IPv4
        with open(output, "w") as f:
            for ip in result:
                f.write(str(ip) + "\n")
    except Exception as e:
        print(f"[!] DNS lookup failed: {e}")

# ---------- Main Program ----------
def main():
    # รับค่า argument จาก command line เช่น: python recon.py example.com
    if len(sys.argv) != 2:
        print("Usage: python recon.py <target>")
        sys.exit(1)

    target = sys.argv[1]

    # ป้องกันผู้ใช้ใส่ target แบบผิด เช่น มีโปรโตคอลหรือ path
    if target.startswith("http://") or target.startswith("https://") or "/" in target:
        print("[!] Please input only IP or domain name. Example: 192.168.1.10 or example.com")
        sys.exit(1)

    print(f"[+] Starting recon on target: {target}")
    output_path = create_output_dir(target)

    # เรียกใช้แต่ละขั้นตอน recon
    nmap_scan(target, output_path)
    print("[DEBUG] เริ่ม Gobuster แล้ว...")
    gobuster_scan(target, output_path)
    whois_lookup(target, output_path)
    dig_lookup(target, output_path)

    print(f"\n[✔] Recon complete! Results saved in: {output_path}")

# ---------- เรียก main เมื่อรันไฟล์โดยตรง ----------
if __name__ == "__main__":
    print("[DEBUG] เรียก main() แล้วนะ")
    main()
