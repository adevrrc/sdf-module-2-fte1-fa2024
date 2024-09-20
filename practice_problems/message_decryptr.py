"""
Description: This script decrypt a message entered by the user.
Author: Damien Altenburg
Date: 2024-9-18
Usage: python message_decrytpr.py
"""
encrypted_message = input("Enter the encrypted message: ")

# Hiejlzl3ow
# 01234567890123456
# H e l l o

""" decrypted_message = encrypted_message[0] + encrypted_message[2] + \
                    encrypted_message[4] + encrypted_message[6] + \
                    encrypted_message[8] """

decrypted_message = encrypted_message[0:9:2]

print(f"Decrypted message> {decrypted_message}")
