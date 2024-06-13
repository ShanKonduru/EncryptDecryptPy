import EncryptDecrypt
from cryptography.fernet import Fernet

# Ensure the key is properly URL-safe base64 encoded (remove padding if necessary)
key = Fernet.generate_key()
encryptor = EncryptDecrypt.EncryptDecryptString(key)

original_usn = "Bhu0018"
encrypted_usn = encryptor.encrypt(original_usn)
decrypted_usn = encryptor.decrypt(encrypted_usn)

print(f"Original key: {key}")
print(f"Original message: {original_usn}")
print(f"Encrypted message: {encrypted_usn}")  # This will not be readable
print(f"Decrypted message: {decrypted_usn}")

original_pwd = "WelcomeToCanada"
encrypted_pwd = encryptor.encrypt(original_pwd)
decrypted_pwd = encryptor.decrypt(encrypted_pwd)

print(f"Original key: {key}")
print(f"Original message: {original_pwd}")
print(f"Encrypted message: {encrypted_pwd}")  # This will not be readable
print(f"Decrypted message: {decrypted_pwd}")
