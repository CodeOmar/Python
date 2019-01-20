alphabet = 'abcdefghijklmnopqrstuvwxyz'
new_message = ' '

# user inputs number to encrypt key
key = int(input('Enter key number: '))
print('Key number: ', key)

# user inputs message
message = input('Enter a message to encrypt: ')
for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        new_position = (position + key) % 26
        new_character = alphabet[new_position]
        new_message += new_character
    else:
        new_message += character

print('Encrypted message: ', new_message)

# Caesar cipher swaps letters around by using the numerical key inputted to create a new character
