import string
 
def encryption(message, encryption_code = 2):
    default_index = string.ascii_lowercase
    encrypted_word = ""
 
    for x in range(len(message)):
        if message[x] in default_index:
            original_position = default_index.index(message[x])
            new_index = (original_position + encryption_code) % 26
            encrypted_word += default_index[new_index]
        else:
            encrypted_word += message[x]
 
    return encrypted_word
 
 
message = input("Enter your message: ").lower()
encryption_code = int(input("Enter the encryption shift: "))
 
encrypted_result = encryption(message, encryption_code)
print("Encrypted word is:", encrypted_result)
 
