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


# def recover_plaintext_pin(decrypted_pin_block, offset, decimalization_table):
#     """
#     Recover plaintext PIN from decrypted PIN block, offset, and decimalization table.
#
#     :param decrypted_pin_block: The decrypted PIN block (hexadecimal string).
#     :param offset: The offset (string of digits).
#     :param decimalization_table: The decimalization table (string of 16 digits).
#     :return: The plaintext PIN.
#     """
#     # Convert the decrypted PIN block to digits using the decimalization table
#     pin_digits = [decimalization_table[int(char, 16)] for char in decrypted_pin_block]
#
#     # Apply the offset to recover the plaintext PIN
#     plaintext_pin = ''.join(str((int(pin_digits[i]) - int(offset[i])) % 10) for i in range(len(offset)))
#
#     return plaintext_pin
#
#
# # Example inputs
# decrypted_pin_block = "12345678"  # Example decrypted block (replace with actual)
# offset = "5493"
# decimalization_table = "0123456789012345"
#
# # Recover the PIN
# plaintext_pin = recover_plaintext_pin(decrypted_pin_block, offset, decimalization_table)
# print(f"Recovered Plaintext PIN: {plaintext_pin}")
