import tkinter as tk

window = tk.Tk()


def key():
    key1 = int(entry1.get())
    return key1


def display1():
    key_num = key()
    key_display = tk.Text(master=window, height=2, width=5)
    key_display.grid(column=3, row=0)
    key_display.insert(tk.END, key_num)


def enter():
    key1 = key()
    new_message = ''
    message = str(entry2.get())
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for character in message:
            if character in alphabet:
                position = alphabet.find(character)
                new_position = (position + key1) % 26
                new_character = alphabet[new_position]
                new_message += new_character
            else:
                new_message += character
    return new_message


def display2():
    encrypt = enter()

    encrypt_display = tk.Text(master=window, height=15, width=40)
    encrypt_display.grid(column=1, row=6)
    encrypt_display.insert(tk.END, encrypt)

# Title of the GUI
window.title('Casear Encryption')
# Size of the window
window.geometry('600x600')

# label for key
title_key = tk.Label(text='Enter key number: ')
title_key.grid(column=0, row=0)

# entry field for key
entry1 = tk.Entry()
entry1.grid(column=1, row=0)

# button for key
button1 = tk.Button(text='Enter', command=display1)
button1.grid(column=1, row=1)

# label for encrypt
title = tk.Label(text='Enter message to encrypt: ')
title.grid(column=0, row=3)

# entry field for encrypt
entry2 = tk.Entry()
entry2.grid(column=1, row=3)

# button for encrypt
button2 = tk.Button(text='Enter', command=display2)
button2.grid(column=1, row=4)

# label for key entered
title_key_entered = tk.Label(text='Key entered: ')
title_key_entered.grid

# runs everything inside window
window.mainloop()
