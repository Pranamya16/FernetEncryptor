# FernetEncryptor

A secure Python-based text encryption tool using the Fernet symmetric encryption algorithm (AES-128-CBC + HMAC-SHA256).

## Features

- 🔐 Secure text encryption using Fernet (AES-128)
- 🔑 Key generation and management
- 💾 Save and load encryption keys
- 🔄 Encrypt and decrypt text messages
- 🖥️ Interactive command-line interface
- ✅ Data integrity verification with HMAC

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Pranamya16/FernetEncryptor.git
cd FernetEncryptor
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the program:
```bash
python code.py
```

### Basic Workflow

1. **Generate a new encryption key** (Option 1)
2. **Encrypt your text** (Option 3)
3. **Save your key** (Option 5) - Important: Keep it safe!
4. **Decrypt text** (Option 4) using the same key

### Example

```
Options:
1. Generate new encryption key
2. Load existing key from file
3. Encrypt text
4. Decrypt text
5. Save key to file
6. Display current key
7. Exit

Enter your choice (1-7): 1
New key generated successfully!

Enter your choice (1-7): 3
Enter text to encrypt: Hello World!
✓ Encrypted text:
gAAAAABmX9k2J...
```

## Security Features

- **AES-128-CBC**: Industry-standard symmetric encryption
- **HMAC-SHA256**: Message authentication and integrity verification
- **Random IV**: Each encryption produces unique output
- **Timestamp**: Built-in message expiration capability

## Project Structure

```
FernetEncryptor/
├── code.py    # Main program file
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── LICENSE             # License information
└── .gitignore          # Git ignore rules
```

## Important Notes

⚠️ **Keep your encryption key safe!**
- Without the key, encrypted data cannot be recovered
- Store keys in a secure location
- Never share keys in public repositories
- Consider using environment variables for key storage in production

## Technologies Used

- Python 3.x
- cryptography library (Fernet)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is intended for educational purposes and personal use. Always ensure you understand the security implications when handling sensitive data.

## Author

Pranamya Deshpande

Project Link: [https://github.com/yourusername/text-encryption-program](https://github.com/Pranamya16/FernetEncryptor)

## Acknowledgments

- Built with the [cryptography](https://cryptography.io/) library
- Inspired by the need for simple, secure text encryption

---

**requirements.txt**
```
cryptography>=41.0.0
```

---

**.gitignore**
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
ENV/
env/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# Encryption Keys (IMPORTANT!)
*.key
encryption_key.key

# OS
.DS_Store
Thumbs.db

# Logs
*.log
```

---

**LICENSE (MIT License)**
```
MIT License

Copyright (c) 2025 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

**CONTRIBUTING.md** (Optional but professional)
```markdown
# Contributing to Text Encryption Program

Thank you for considering contributing to this project! 

## How to Contribute

1. **Fork the Repository**
   - Click the 'Fork' button at the top right of the repository page

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/yourusername/text-encryption-program.git
   ```

3. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Your Changes**
   - Write clean, documented code
   - Follow Python PEP 8 style guidelines
   - Add comments where necessary

5. **Test Your Changes**
   - Ensure the program runs without errors
   - Test all functionalities

6. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

7. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Submit a Pull Request**
   - Go to the original repository
   - Click 'New Pull Request'
   - Describe your changes

## Code Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and small

## Reporting Issues

- Use the GitHub Issues tab
- Provide clear description
- Include steps to reproduce
- Mention your Python version

Thank you for your contributions!
```
