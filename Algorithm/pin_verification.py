from cryptography.fernet import Fernet

# Generate a key for encryption and decryption (usually saved securely in a real system)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

print(key)
print(cipher_suite)


def encrypt_pin(pin):
    """Encrypt the PIN using the symmetric key."""
    return cipher_suite.encrypt(pin.encode())


def decrypt_pin(encrypted_pin):
    """Decrypt the PIN using the symmetric key."""
    return cipher_suite.decrypt(encrypted_pin).decode()


def verify_pin(stored_encrypted_pin, input_pin):
    """
    Verify the user-provided PIN against the encrypted stored PIN.

    :param stored_encrypted_pin: The encrypted PIN stored securely.
    :param input_pin: The PIN entered by the user.
    :return: True if the PIN matches, False otherwise.
    """
    decrypted_pin = decrypt_pin(stored_encrypted_pin)
    return decrypted_pin == input_pin


# Example usage
# if __name__ == "__main__":
#     # Simulate setting up an account with a PIN
#     original_pin = "1234"  # Example PIN (ideally chosen by the user)
#     encrypted_pin = encrypt_pin(original_pin)
#     print("Encrypted PIN stored:", encrypted_pin)
#
#     # Simulate user attempting to log in
#     user_input = input("Enter your PIN: ")
#
#     if verify_pin(encrypted_pin, user_input):
#         print("PIN verified successfully!")
#     else:
#         print("Invalid PIN.")
