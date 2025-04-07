"""
USING TWO DIFFERENT FUNCTIONS ENCRYPTION AND DECRYPTION

"""



'''alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
             'u', 'v', 'w', 'x', 'y', 'z']

def encryption(message,key):  
    encryt_message = ""
    for char in message:
        if char in alphabets:
            char_index = alphabets.index(char)
            enc_index = (char_index + user_key) % 26
            encryt_message += alphabets[enc_index]
        else:
            encryt_message += char
    print("Encrypted_message:",encryt_message)

def decryption(message,key):
    decrypt_message = ""
    for char in message:
        if char in alphabets:
            char_index = alphabets.index(char)
            dec_index = (char_index - user_key) % 26
            decrypt_message += alphabets[dec_index]
        else:
            decrypt_message += char
    print("Decrypt_message:",decrypt_message)


# what_to_do = input("Type 'encrypt' for encryption and 'decrypt' for decryption:\n")

Flag = False
while not Flag:
    what_to_do = input('Type \'encrypt\' for encryption and \'decrypt\' for decryption:\n')

    user_msg = input("Enter your message:\n")

    user_key = int(input("Enter the key:\n"))

    if what_to_do == 'encrypt':
        encryption(user_msg,user_key)

    elif what_to_do == 'decrypt':
        decryption(user_msg,user_key)
    
    again_msg = input("Type 'yes' to continue and 'no' to exit:\n")

    if again_msg == 'no' or again_msg == 'No':
        Flag = True
        print("Goodbye, Have a nice day!")'''
    


# -------------------------------------------------------------------------------------------------------------

"""
USING ONLY ONE FUNCTION FOR BOTH ENCRYPTION AND DECRYPTION

"""
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
             'u', 'v', 'w', 'x', 'y', 'z']

def dencrypt(direction,message,key):
    encryt_message = ""
    decrypt_message = ""
    if direction == 'encrypt':
        for char in message:
            if char in alphabets:
                char_index = alphabets.index(char)
                enc_index = (char_index + user_key) % 26
                encryt_message += alphabets[enc_index]
            else:
                encryt_message += char
        print("Encrypt Message:",encryt_message)
    elif direction == 'decrypt':
        for char in message:
            if char in alphabets:
                char_index = alphabets.index(char)
                dec_index = (char_index - user_key) % 26
                decrypt_message += alphabets[dec_index]
            else:
                decrypt_message += char
        print("Decrypt Message:",decrypt_message)


Flag = False
while not Flag:
    what_to_do = input('Type \'encrypt\' for encryption and \'decrypt\' for decryption:\n')

    user_msg = input("Enter your message:\n").lower()

    user_key = int(input("Enter the key:\n"))

    dencrypt(direction=what_to_do,message=user_msg,key=user_key)

    again_msg = input("Type 'yes' to continue and 'no' to exit:\n")

    if again_msg == 'no' or again_msg == 'No':
        Flag = True
        print("Goodbye,Have a nice day!")



# --------------------------------------------------------------------------------------------------

"""
USING ONLY ONE FUNCTION FOR BOTH ENCRYPTION AND DECRYPTION with more precise and accurate results 
using alpha, lower and upper functions
"""

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
             'u', 'v', 'w', 'x', 'y', 'z']

def dencrypt(direction,message,key):
    encryt_message = ""
    decrypt_message = ""
    if direction == 'encrypt':
        for char in message:
            if char.isalpha():
                if char.isupper():
                    char_new = char.lower()
                    if char_new in alphabets:
                        char_new_index = alphabets.index(char_new)
                        enc_index = (char_new_index + key) % 26
                        encryt_message += alphabets[enc_index].upper()
                else:
                    if char in alphabets:
                        char_index = alphabets.index(char)
                        enc_index = (char_index + key) % 26
                        encryt_message += alphabets[enc_index]
                    else:
                        encryt_message += char
            else:
                encryt_message += char

        print("Encrypt Message:",encryt_message)
    elif direction == 'decrypt':
        for char in message:
            if char.isalpha():
                if char.isupper():
                    char_new = char.lower()
                    if char_new in alphabets:
                        char_new_index = alphabets.index(char_new)
                        
                        dec_index = (char_new_index - key) % 26
                        decrypt_message += alphabets[dec_index].upper()
                else:
                    if char in alphabets:
                        char_index = alphabets.index(char)
                        dec_index = (char_index - key) % 26
                        decrypt_message += alphabets[dec_index]
                    else:
                        decrypt_message += char
            else:
                decrypt_message += char
        print("Decrypt Message:",decrypt_message)


Flag = False
while not Flag:
    what_to_do = input('Type \'encrypt\' for encryption and \'decrypt\' for decryption:\n')

    user_msg = input("Enter your message:\n")

    user_key = int(input("Enter the key:\n"))

    dencrypt(direction=what_to_do,message=user_msg,key=user_key)

    again_msg = input("Type 'yes' to continue and 'no' to exit:\n")

    if again_msg == 'no' or again_msg == 'No':
        Flag = True
        print("Goodbye,Have a nice day!")

































    
