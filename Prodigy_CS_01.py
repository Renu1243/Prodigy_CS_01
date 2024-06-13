import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, decrypt=False):
    """
    Encrypts or decrypts the given text using the Caesar Cipher algorithm.
    
    Parameters:
    - text (str): The text to be encrypted or decrypted.
    - shift (int): The shift value for the cipher.
    - decrypt (bool): Flag indicating whether to decrypt (default is False).
    
    Returns:
    - processed_text (str): The processed text (encrypted or decrypted).
    """
    if decrypt:
        shift = -shift  # Reverse the shift for decryption
    
    processed_text = []
    
    for char in text:
        if char.isalpha():
            # Determine the appropriate case (uppercase or lowercase)
            base = ord('A') if char.isupper() else ord('a')
            # Apply the shift and ensure it wraps around the alphabet
            processed_text.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            processed_text.append(char)  # Leave non-alphabet characters unchanged
    
    return ''.join(processed_text)

def encrypt_text():
    input_text = text_entry.get("1.0", "end-1c")  # Get the text from the input field
    try:
        shift_value = int(shift_entry.get())  # Get the shift value from the input field
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for the shift value.")
        return
    
    encrypted_text = caesar_cipher(input_text, shift_value)
    output_text.delete("1.0", "end")  # Clear any previous output
    output_text.insert("1.0", encrypted_text)

def decrypt_text():
    input_text = text_entry.get("1.0", "end-1c")  # Get the text from the input field
    try:
        shift_value = int(shift_entry.get())  # Get the shift value from the input field
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for the shift value.")
        return
    
    decrypted_text = caesar_cipher(input_text, shift_value, decrypt=True)
    output_text.delete("1.0", "end")  # Clear any previous output
    output_text.insert("1.0", decrypted_text)

# Create the main window
root = tk.Tk()
root.title("Caesar Cipher Tool")

# Create labels and entries for input text and shift value
tk.Label(root, text="Enter Text:").pack()
text_entry = tk.Text(root, height=5, width=50)
text_entry.pack()

tk.Label(root, text="Enter Shift Value:").pack()
shift_entry = tk.Entry(root)
shift_entry.pack()

# Create buttons for encryption and decryption
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.pack()

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.pack()

# Create a text area for displaying output
tk.Label(root, text="Output:").pack()
output_text = tk.Text(root, height=5, width=50)
output_text.pack()

# Run the main loop
root.mainloop()
