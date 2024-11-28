from cryptography.fernet import Fernet
from colorama import Back, Fore

# Generate a key for encryption and decryption (usually saved securely in a real system)
key = Fernet.generate_key()
cipher_suite = Fernet(key)


def encrypt_pin(pin):
    return cipher_suite.encrypt(pin.encode())


def decrypt_pin(encrypted_pin_number):
    return cipher_suite.decrypt(encrypted_pin_number).decode()


def verify_pin(stored_encrypted_pin, input_pin):
    decrypted_pin = decrypt_pin(stored_encrypted_pin)
    return decrypted_pin == input_pin


def main():
    # Simulate setting up an account with a PIN
    original_pin = "12345"  # Example PIN (ideally chosen by the user)
    encrypted_pin = encrypt_pin(original_pin)

    # Simulate user attempting to log in
    user_input = input(Fore.CYAN+ "Enter your PIN: ")

    if verify_pin(encrypted_pin, user_input):
        print(Fore.GREEN+ "PIN verified successfully!")
    else:
        print(Fore.RED+ "Invalid PIN.")
        main()


# Example usage
if __name__ == "__main__":
    main()
