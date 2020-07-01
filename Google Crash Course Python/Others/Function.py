# def Namata():
#     a = input('what is the range of your Namata: ')
#     c = input('how much it will be Iterate: ')
#     for i in range(int(a)):
#         if i == 0:
#             continue
#         for j in range(int(c)):
#             if j == 0:
#                 continue
#             b = i * j
#             print('{} X {} = {}'.format(i, j, b))
#         print(' ')
#
# Namata()


# If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one byte will still use 4096 bytes of storage.
# A file made up of 4097 bytes will use 4096*2=8192 bytes of storage.
# Knowing this, can you fill in the gaps in the calculate_storage function below
# which calculates the total number of bytes needed to store a file of a given size?

"""def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize/block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize%block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return 4096*(full_blocks+1)
    return full_blocks*block_size

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192"""

"""
def format_name(first_name, last_name):
    if first_name and last_name:
        return f"Name: {last_name}, {first_name}"
    elif first_name or last_name:
        return f"Name: {first_name}{last_name}"
    else: 
        return ""

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string
"""



'''def fractional_part(numerator, denominator):
    if denominator == 0:
        return 0
    else:
        return ((numerator / denominator) - (numerator // denominator))


print(fractional_part(5, 5))  # Should be 0
print(fractional_part(5, 4))  # Should be 0.25
print(fractional_part(5, 3))  # Should be 0.66...
print(fractional_part(5, 2))  # Should be 0.5
print(fractional_part(5, 0))  # Should be 0
print(fractional_part(0, 5))  # Should be 0'''
