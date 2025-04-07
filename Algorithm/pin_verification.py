from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.fernet import Fernet
from colorama import Back, Fore


#
# # Generate a key for encryption and decryption (usually saved securely in a real system)
# key = Fernet.generate_key()
# cipher_suite = Fernet(key)
#
#
# def encrypt_pin(pin):
#     return cipher_suite.encrypt(pin.encode())
#
#
# def decrypt_pin(encrypted_pin_number):
#     return cipher_suite.decrypt(encrypted_pin_number).decode()
#
#
# def verify_pin(stored_encrypted_pin, input_pin):
#     decrypted_pin = decrypt_pin(stored_encrypted_pin)
#     return decrypted_pin == input_pin
#
#
# def main():
#     # Simulate setting up an account with a PIN
#     original_pin = "12345"  # Example PIN (ideally chosen by the user)
#     encrypted_pin = encrypt_pin(original_pin)
#
#     # Simulate user attempting to log in
#     user_input = input(Fore.CYAN+ "Enter your PIN: ")
#
#     if verify_pin(encrypted_pin, user_input):
#         print(Fore.GREEN+ "PIN verified successfully!")
#     else:
#         print(Fore.RED+ "Invalid PIN.")
#         main()
#
#
# # Example usage
# if __name__ == "__main__":
#     main()


def decrypt(key, data):
    # Placeholder function for decryption
    return data  # Replace with actual decryption logic


def encrypt(key, data):
    # Placeholder function for encryption
    return data  # Replace with actual encryption logic


def format_check(data):
    # Placeholder function for format checking
    # Return None if format is invalid, else return processed data
    return data if data else None


def decimalize(dectab, hex_str):
    # Convert hexadecimal string to decimal using dectab
    return int(''.join(dectab[int(c, 16)] for c in hex_str), 10)


def sum_mod10(value, offset):
    # Calculate the sum modulo 10
    return (value + offset) % 10


def PIN(EPB, vdata, length, dectab, offset, key):
    # Decrypt the typed PIN
    x1 = decrypt(key, EPB)

    # Check format and remove random data
    t_pin = format_check(x1)
    if t_pin is None:
        return "Format wrong"

    # Encrypt vdata
    x2 = encrypt(vdata)

    # Take the leftmost 'length' hex digits
    x3 = x2[:length]

    # Decimalize the digits
    x4 = decimalize(dectab, x3)

    # Compute the user PIN with offset
    u_pin = sum_mod10(x4, offset)

    # Compare t_pin and u_pin
    if t_pin == u_pin:
        return "PIN is correct"
    else:
        return "PIN is incorrect"


# Example usage (placeholders)
EPB = "encrypted_pin_blob"
vdata = "verification_data"
length = 5
dectab = {i: str(i) for i in range(16)}  # Placeholder decimalization table
offset = 3
key = "encryption_key"

print(PIN(EPB, vdata, length, dectab, offset, key))
