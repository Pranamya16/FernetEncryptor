from cryptography.fernet import Fernet
import base64
import os

class TextEncryptor:
    def __init__(self):
        self.key = None
        self.cipher = None

    def generate_key(self):
        """Generate a new encryption key"""
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)
        return self.key

    def load_key(self, key):
        """Load an existing encryption key"""
        self.key = key
        self.cipher = Fernet(self.key)

    def encrypt_text(self, text):
        """Encrypt the given text"""
        if self.cipher is None:
            raise ValueError("No encryption key loaded. Generate or load a key first.")

        # Convert text to bytes and encrypt
        text_bytes = text.encode('utf-8')
        encrypted_bytes = self.cipher.encrypt(text_bytes)

        # Return as base64 string for easy display
        return encrypted_bytes.decode('utf-8')

    def decrypt_text(self, encrypted_text):
        """Decrypt the given encrypted text"""
        if self.cipher is None:
            raise ValueError("No encryption key loaded. Generate or load a key first.")

        # Convert encrypted text to bytes and decrypt
        encrypted_bytes = encrypted_text.encode('utf-8')
        decrypted_bytes = self.cipher.decrypt(encrypted_bytes)

        # Return as string
        return decrypted_bytes.decode('utf-8')

    def save_key_to_file(self, filename="encryption_key.key"):
        """Save the encryption key to a file"""
        with open(filename, 'wb') as key_file:
            key_file.write(self.key)
        print(f"Key saved to {filename}")

    def load_key_from_file(self, filename="encryption_key.key"):
        """Load the encryption key from a file"""
        with open(filename, 'rb') as key_file:
            self.key = key_file.read()
            self.cipher = Fernet(self.key)
        print(f"Key loaded from {filename}")


def main():
    encryptor = TextEncryptor()

    print("=" * 50)
    print("TEXT ENCRYPTION PROGRAM")
    print("=" * 50)

    while True:
        print("\nOptions:")
        print("1. Generate new encryption key")
        print("2. Load existing key from file")
        print("3. Encrypt text")
        print("4. Decrypt text")
        print("5. Save key to file")
        print("6. Display current key")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ").strip()

        if choice == '1':
            key = encryptor.generate_key()
            print("\nNew key generated successfully!")
            print(f"Key: {key.decode('utf-8')}")
            print("\n⚠️  IMPORTANT: Save this key! You'll need it to decrypt your messages.")

        elif choice == '2':
            filename = input("Enter key filename (press Enter for 'encryption_key.key'): ").strip()
            if not filename:
                filename = "encryption_key.key"
            try:
                encryptor.load_key_from_file(filename)
            except FileNotFoundError:
                print(f"Error: File '{filename}' not found.")
            except Exception as e:
                print(f"Error loading key: {e}")

        elif choice == '3':
            if encryptor.cipher is None:
                print("\nError: No encryption key loaded. Please generate or load a key first.")
                continue

            text = input("\nEnter text to encrypt: ")
            try:
                encrypted = encryptor.encrypt_text(text)
                print("\n✓ Encrypted text:")
                print(encrypted)
            except Exception as e:
                print(f"Error encrypting text: {e}")

        elif choice == '4':
            if encryptor.cipher is None:
                print("\nError: No encryption key loaded. Please generate or load a key first.")
                continue

            encrypted_text = input("\nEnter encrypted text to decrypt: ")
            try:
                decrypted = encryptor.decrypt_text(encrypted_text)
                print("\n✓ Decrypted text:")
                print(decrypted)
            except Exception as e:
                print(f"Error decrypting text: {e}")
                print("Make sure you're using the correct key and encrypted text.")

        elif choice == '5':
            if encryptor.key is None:
                print("\nError: No key to save. Generate a key first.")
                continue

            filename = input("Enter filename to save key (press Enter for 'encryption_key.key'): ").strip()
            if not filename:
                filename = "encryption_key.key"
            try:
                encryptor.save_key_to_file(filename)
            except Exception as e:
                print(f"Error saving key: {e}")

        elif choice == '6':
            if encryptor.key:
                print(f"\nCurrent key: {encryptor.key.decode('utf-8')}")
            else:
                print("\nNo key currently loaded.")

        elif choice == '7':
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
