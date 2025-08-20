# 🔓 Hash Cracker
A powerful Python-based hash cracking tool that supports multiple cryptographic algorithms and uses dictionary attacks to recover original strings from hashed values.


<img width="1116" height="626" alt="Screenshot 2025-08-20 192715" src="https://github.com/user-attachments/assets/ca37c236-c5c6-41bd-96d1-26c7adcd0257" />

# ✨ Features
+ 🔢 Multiple Algorithm Support: MD5, SHA1, SHA256, SHA512, and more via Python's hashlib

+ 🎨 Colorized Interface: Clear visual feedback with color-coded outputs using Colorama

+ 📚 Wordlist Attacks: Dictionary-based cracking with support for large wordlists

+ 🚨 Comprehensive Error Handling: Graceful handling of file operations and invalid inputs

+ 🌍 UTF-8 Encoding Support: International wordlist compatibility

# 🚀 Installation
Clone the repository:

```
git clone https://github.com/CodeZANKO/hash-Zan.git
cd Hash-Zan
```
Install dependencies:

```
pip install -r requirements.txt
```
# 💻 Usage
Run the script and follow the interactive prompts:

```
python main.py
```
You'll be prompted for:

The target hash to crack

Hash algorithm type (md5, sha1, sha256, sha512, etc.)

Path to your wordlist file

# 🧮 Supported Hash Algorithms
This tool supports all algorithms available in Python's hashlib module:<br/>

Algorithm Family |	Specific Algorithms<br/>
__________________________________<br/>
MD	             | MD5<br/>
SHA	             | SHA1, SHA224, SHA256, SHA384, SHA512<br/>
SHA3	         | SHA3-224, SHA3-256, SHA3-384, SHA3-512<br/>
BLAKE	         | BLAKE2b, BLAKE2s<br/>
Other	         | All other hashlib supported algorithms<br/>
# 📋 Example
```
Enter Your Hash: 5d41402abc4b2a76b9719d911017c592
Type Of hash (Eg:md5,sha1): md5
Path of wordlist: /path/to/wordlist.txt
Hash is Cracked: hello
```
# 📦 Requirements
Python 3.6+

colorama (for colored terminal output)

hashlib
# 📁 Project Structure
text
hash-cracker/
├── hash_cracker.py    # Main application<br/>
├── requirements.txt   # Dependencies<br/>
├── LICENSE           # License file<br/>
├── README.md         # Project documentation<br/>
└── wordlists/        # Directory for wordlists (optional)<br/>
    ├── common.txt<br/>
    └── passwords.txt<br/>
# 🤝 Contributing
Contributions are welcome! Feel free to:

Fork the project

Create a feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

Please read our Contributing Guidelines for details.

# ⚠️ Disclaimer
This tool is intended for:

Educational purposes and security research

Password recovery on your own systems

Authorized penetration testing and security assessments

Always ensure you have explicit permission before testing any system. Never use this tool for unauthorized access attempts or malicious activities.

The developers assume no liability and are not responsible for any misuse or damage caused by this program.

# 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

<div align="center"> Made with ❤️ and Python </div>
