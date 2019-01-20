alphabet = 'abcdefghijklmnopqrstuvwxyz'
new_message = ' '

key = int(input('Enter key number: '))
print('Key number: ', key)

message = input('Enter encrypted message: ')
for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        new_position = (position - key) % 26
        new_character = alphabet[new_position]
        new_message += new_character
    else:
        new_message += character

print('Decrypted message: ', new_message)
