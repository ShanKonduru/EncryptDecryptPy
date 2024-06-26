# EncryptDecryptString

EncryptDecryptString is a Python class for easily encrypting and decrypting strings using the Fernet symmetric encryption algorithm from the cryptography library.

## Installation

You can install EncryptDecryptString via pip:

```bash
pip install encryptdecryptstring
```

## Usage

```bash
from encryptdecryptstring import EncryptDecryptString

# Initialize EncryptDecryptString with a secret key
key = b'your_secret_key_here'  # Replace 'your_secret_key_here' with an actual secret key
encryptor = EncryptDecryptString(key)

# Encrypt a message
encrypted_message = encryptor.encrypt("Hello, world!")

# Decrypt the encrypted message
decrypted_message = encryptor.decrypt(encrypted_message)

print(decrypted_message)  # Output: Hello, world!

```

## How to Generate a Secret Key

To generate a secret key, you can use the Fernet.generate_key() method provided by the cryptography library. Here's an example:

```bash
from cryptography.fernet import Fernet

# Generate a secret key
key = Fernet.generate_key()

print(key)  # Output: b'...'
```
Replace your_secret_key_here with the generated key.

## Contributing
Contributions are welcome! If you find a bug or have a suggestion for improvement, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

```bash
This README.md provides clearer instructions on how to install and use the package, including how to generate a secret key.
```
