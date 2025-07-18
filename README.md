# =================== README.md ===================

# 🛠️ Python Reverse Shell Backdoor (Ethical Pentest Project)

This project is a Python-based **reverse shell backdoor** designed for ethical hacking labs, penetration testing simulations, and red team learning environments. It allows secure remote access, file operations, and keylogging functionalities.

> ⚠️ **DISCLAIMER**: This tool is developed strictly for **educational purposes** and **authorized testing environments only**. Unauthorized deployment or use may violate computer misuse laws.

---

## 🚀 Features

- 🔐 **AES-Encrypted Communication** – Secure transmission between client and server using AES (ECB).
- 🖥️ **Remote Shell Access** – Execute OS-level commands remotely on the target system.
- 📂 **File Transfer** – Upload/download files between attacker and target.
- 🔑 **Keylogger** – Captures and transmits keystrokes using the `pynput` module.
- 🧠 **Virtual Machine Detection** – Identifies execution in VM environments (VMware, VirtualBox, QEMU).
- 🎭 **Obfuscated System Shutdown** – Executes encoded shutdown commands (Windows/Linux).
- ⏱️ **Randomized Beacon Delay** – Adds stealth with varied connection attempts.
- 🧊 **Executable Packing** – Compiled with PyInstaller and UPX to reduce antivirus detection.

---

## 📁 File Structure

- `backdoor.py` – The client payload running on the victim machine.
- `server.py` – The command-and-control interface used by the attacker.

---

## 🛠️ Setup Instructions

### ✅ Requirements
Install required modules:
```bash
pip install pynput pycryptodome
```

### 🔒 Generate Executable (Windows)
```bash
pyinstaller backdoor.py --onefile --noconsole
upx --best --ultra-brute dist/backdoor.exe
```

> Optional: Add `--icon=youricon.ico` to customize the executable.

---

## 💻 Usage

1. **Start the server**:
```bash
python server.py
```

2. **Deploy the backdoor** (client) on the target machine.

3. **Available commands from server**:
   - `cd <path>` – Change directory
   - `upload <filename>` – Send file to victim
   - `download <filename>` – Get file from victim
   - `keylog` – Dump keystroke logs
   - `poweroff` – Shutdown target system
   - `clear`, `quit`, or any shell command (e.g. `dir`, `ls`, `ipconfig`)

---

## ⚔️ For Ethical Use Only
This tool was created to understand attacker methodologies and develop stronger defenses. Always use in **sandboxed, consented** environments.

---

## 🧠 Author
Shlok Jadhav  
[LinkedIn](https://www.linkedin.com/in/shlokjadhav42)

---

## 📜 License
This project is for **educational and research use** only. Do not use in unauthorized environments. The author is not responsible for any misuse.
