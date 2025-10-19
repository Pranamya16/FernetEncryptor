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


