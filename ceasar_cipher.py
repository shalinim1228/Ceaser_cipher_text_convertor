import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Ensure Pillow is installed and updated

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    return cipher_text

def decryption(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_key) % 26
            plain_text += alphabet[new_position]
        else:
            plain_text += char
    return plain_text

def encrypt_message():
    text = entry_message.get().lower()
    try:
        shift = int(entry_shift.get())
        encrypted = encryption(text, shift)
        messagebox.showinfo("Encryption Result", f"Encrypted message: {encrypted}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid shift number.")

def decrypt_message():
    text = entry_message.get().lower()
    try:
        shift = int(entry_shift.get())
        decrypted = decryption(text, shift)
        messagebox.showinfo("Decryption Result", f"Decrypted message: {decrypted}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid shift number.")

def clear_fields():
    entry_message.delete(0, tk.END)
    entry_shift.delete(0, tk.END)

# Initialize the window
window = tk.Tk()
window.title("Caesar Cipher - Encryption & Decryption")
window.geometry("400x300")

# Load the background image
bg_image = Image.open("download.jpg")  # Ensure the image file exists
bg_image = bg_image.resize((400, 300), Image.Resampling.LANCZOS)  # Resize the image to fit the window
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label to hold the background image
bg_label = tk.Label(window, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)  # Stretch to fit the window

# Label and entry for the message
label_message = tk.Label(window, text="Enter your message:", bg="lightblue", font=("Arial", 12))
label_message.pack(pady=10)
entry_message = tk.Entry(window, width=40, font=("Arial", 12))
entry_message.pack(pady=5)

# Label and entry for the shift number
label_shift = tk.Label(window, text="Enter shift number:", bg="lightblue", font=("Arial", 12))
label_shift.pack(pady=10)
entry_shift = tk.Entry(window, width=10, font=("Arial", 12))
entry_shift.pack(pady=5)

# Encrypt and Decrypt buttons
button_encrypt = tk.Button(window, text="Encrypt", command=encrypt_message, font=("Arial", 12), bg="#051d73", fg="white")
button_encrypt.pack(pady=10)

button_decrypt = tk.Button(window, text="Decrypt", command=decrypt_message, font=("Arial", 12), bg="#390573", fg="white")
button_decrypt.pack(pady=10)

# Clear button
button_clear = tk.Button(window, text="Clear", command=clear_fields, font=("Arial", 12), bg="#3f0458", fg="white")
button_clear.pack(pady=10)

# Run the application
window.mainloop()
