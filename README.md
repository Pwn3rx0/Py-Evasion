# PyPayload-Evasion

A Python utility designed to extract, deobfuscate, and repackage Meterpreter payloads. This tool identifies encoded blobs (Zlib, Base64, or Hex) within a script, extracts the original source, and allows for the generation of a fresh, obfuscated wrapper to evade static analysis by Windows Defender and other AV engines.

## Features
- **Recursive Decoding:** Unpacks nested Base64, Zlib, and Hex layers automatically.
- **Evasion Mode:** Wraps raw code in a Base64 `exec()` loop to mask signatures.
- **Clean Mode:** Extracts raw source for analysis.

---

## Installation
Clone the repository:

```Bash

git clone https://github.com/yourusername/PyPayload-Evasion.git
cd PyPayload-Evasion
```
No external dependencies are required (uses standard Python libraries).

## Usage
```bash
python3 PyEvasion.py -i input.py -o output.py -m evasion
```
----
## ⚠️ Disclaimer
For educational and authorized security testing only. Misuse is illegal.
