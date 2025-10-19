"""
Enforcing privacy with cryptography
"""

user_key = input("Enter your four digit pin: ")

if user_key == 4:	
	user_keys = [(int(count) + 7) % 10 for count in user_key]
user_keys[0],user_keys[2] = user_keys[2],user_keys[0] 
user_keys[1], user_keys[3] = user_keys[3],user_keys[1]
print("Encrypted key: ",user_keys)
#else:
print("Invalid input, Enter a four digit number")


decrypted_key = [((int(counter) - 7) + 10) % 10 for counter in user_keys]
decrypted_key[0],decrypted_key[2] = decrypted_key[2],decrypted_key[0] 
decrypted_key[1], decrypted_key[3] = decrypted_key[3],decrypted_key[1]

print("Decrypted key: ",decrypted_key)

