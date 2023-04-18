user_input = input("Enter a secret message: ")

encrypted_msg = "".join([chr(ord(character) + 3) for character in user_input])
decrypted_msg = "".join([chr(ord(character) - 3) for character in encrypted_msg])

print(f"Encrypted message: {encrypted_msg}")
print(f"Decrypted message: {decrypted_msg}")
