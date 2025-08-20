# Hash Cracker Tool<br/>
A lightweight Python-based hash cracking tool that supports multiple hash algorithms and uses wordlist attacks to recover original strings from hashes.

Features
Multiple Hash Support: Works with MD5, SHA1, SHA256, and other algorithms available in Python's hashlib

Wordlist Attacks: Uses dictionary-based attacks for efficient cracking

User-Friendly Interface: Color-coded terminal output using Colorama

Error Handling: Comprehensive error handling for file operations and hash type validation

# Usage
Clone the repository

Install dependencies: `pip install colorama & hashlib` or `pip install -r requirements.txt`

Run the script: python main.py

Provide:

The target hash

Hash type (md5, sha1, sha256, etc.)

Path to your wordlist file (Most Wordlist[Rockyou] (https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt))

Example
```
Enter Your Hash: 5d41402abc4b2a76b9719d911017c592
Type Of hash (Eg:md5,sha1): md5
Path of wordlist: wordlists/common_passwords.txt
Hash is Cracked: hello
```
# Requirements
Python 3.x<br/>
Hashlib<br/>
Colorama library

# Disclaimer
This tool is intended for educational purposes and legitimate security testing only. Always ensure you have proper authorization before testing any system.
