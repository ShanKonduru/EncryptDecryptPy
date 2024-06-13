from cryptography.fernet import Fernet

class EncryptDecryptString:

  def __init__(self, key):
    self.key = key # .encode()  # Ensure key is a byte string
    self.fernet = Fernet(self.key)

  def encrypt(self, message):
    """
    Encrypts a string message.

    Args:
      message: The string message to encrypt.

    Returns:
      The encrypted message as a byte string.
    """
    message = message.encode()  # Encode to bytes for encryption
    encrypted_message = self.fernet.encrypt(message)
    return encrypted_message

  def decrypt(self, encrypted_message):
    """
    Decrypts an encrypted message.

    Args:
      encrypted_message: The encrypted message as a byte string.

    Returns:
      The decrypted message as a string.
    """
    decrypted_message = self.fernet.decrypt(encrypted_message)
    return decrypted_message.decode()  # Decode from bytes

