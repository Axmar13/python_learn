import re
def rot13(message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ciphered_message = ""
    for char in message:
        if re.match(r'^[ 0-9!@#$%^&*~()_+{}|:"<>?`\-=[\]\\;\',./]+$', char):   ciphered_message += char
        else:  
            if char in alphabet: 
                index = alphabet.find(char) + 13
                if index > len(alphabet):
                    index = index - len(alphabet)
                ciphered_message += alphabet[index % len(alphabet)]
            else:
                index = alphabet.find(char.lower()) + 13
                if index > len(alphabet):
                    index = index - len(alphabet)
                ciphered_message += alphabet[index % len(alphabet)].upper()

    return ciphered_message
    
print(rot13('!@#$%^&*+?~()_-+=:;'))