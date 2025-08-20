# 🔓 Hash Cracker
A powerful Python-based hash cracking tool that supports multiple cryptographic algorithms and uses dictionary attacks to recover original strings from hashed values.



# ✨ Features
🔢 Multiple Algorithm Support: MD5, SHA1, SHA256, SHA512, and more via Python's hashlib

🎨 Colorized Interface: Clear visual feedback with color-coded outputs using Colorama

📚 Wordlist Attacks: Dictionary-based cracking with support for large wordlists

🚨 Comprehensive Error Handling: Graceful handling of file operations and invalid inputs

🌍 UTF-8 Encoding Support: International wordlist compatibility

# 🚀 Installation
Clone the repository:

bash
git clone https://github.com/CodeZANKO/hash-Zan.git
cd hash-cracker
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
This tool supports all algorithms available in Python's hashlib module:

Algorithm Family	Specific Algorithms
MD	MD5
SHA	SHA1, SHA224, SHA256, SHA384, SHA512
SHA3	SHA3-224, SHA3-256, SHA3-384, SHA3-512
BLAKE	BLAKE2b, BLAKE2s
Other	All other hashlib supported algorithms
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

# 📁 Project Structure
text
hash-cracker/
├── hash_cracker.py    # Main application
├── requirements.txt   # Dependencies
├── LICENSE           # License file
├── README.md         # Project documentation
└── wordlists/        # Directory for wordlists (optional)
    ├── common.txt
    └── passwords.txt
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
