import random
CHARACTERS = "AÄBCDEFGHIJKLMNOPÖQRSßTÜVWXYZaäbcdefghijklmnoöpqrstuvwxyz0123456789!@#$%&*()-_+=[].{}<>?/\\|:;'\",.,`~ "
def assign_character_ids():
character_ids = {}
for i, char in enumerate(CHARACTERS):
character_ids[char] = i
return character_ids
def convert_to_numbers(text, character_ids):
converted_chars = []
for c in text:
value = character_ids[c]
converted_chars.append(value)
return converted_chars
def encrypt(message, character_ids):
random_bytes = [random.randint(0, 255) for _ in range(len(message))]
key_builder = []
for i in range(len(message)):
index = random_bytes[i] % len(CHARACTERS)
key_builder.append(CHARACTERS[index])
key = ''.join(key_builder)
converted_message_chars = convert_to_numbers(message, character_ids)
converted_key_chars = convert_to_numbers(key, character_ids)
encrypted_message = []
for i in range(len(converted_message_chars)):
message_char = converted_message_chars[i]
key_char = converted_key_chars[i]
encrypted_char = (message_char + key_char) % len(CHARACTERS)
encrypted_message.append(encrypted_char)
encrypted_text = ''.join([CHARACTERS[i] for i in encrypted_message])
return encrypted_text, key
def decrypt(message, key, character_ids):
converted_message_to_numbers = convert_to_numbers(message, character_ids)
converted_key_to_numbers = convert_to_numbers(key, character_ids)
decrypted_message = []
for i in range(len(converted_message_to_numbers)):
message_char_number = converted_message_to_numbers[i]
key_char_number = converted_key_to_numbers[i]
decrypted_char = (message_char_number - key_char_number) % len(CHARACTERS)
if decrypted_char < 0:
decrypted_char += len(CHARACTERS)
decrypted_message.append(decrypted_char)
decrypted_text = ''.join([CHARACTERS[i] for i in decrypted_message])
return decrypted_text
def main():
character_ids = assign_character_ids()
user_message = input("Enter the message to encrypt: ")
encrypted_msg, key = encrypt(user_message, character_ids)
print(f"Encrypted: {encrypted_msg}")
print(f"Single-use Key: {key}")
decryption_key = input("Enter the decryption key: ")
decrypted_msg = decrypt(encrypted_msg, decryption_key, character_ids)
print(f"Decrypted: {decrypted_msg}")
if __name__ == "__main__":
main()
