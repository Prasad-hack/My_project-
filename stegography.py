import os
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Image Encryption & Decryption")
root.geometry("900x600")

bg_image = Image.open("pic.jpg")  
bg_image = bg_image.resize((900, 600), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)  

header = tk.Label(root, text="Secure Hiding Information Using Steganography",
                  font=("Arial", 16, "bold"), fg="black", bg="sky blue")
header.pack(pady=10, fill="x")

top_fields_frame = tk.Frame(root, bg="sky blue")
top_fields_frame.pack(fill="x", padx=0, pady=0)

tk.Label(top_fields_frame, text="Secret Message:", bg="white", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=0, pady=0)
secret_msg_entry = tk.Entry(top_fields_frame, width=40, font=("Arial", 10))
secret_msg_entry.grid(row=0, column=1, padx=5, pady=0)

tk.Label(top_fields_frame, text="Password:", bg="white", font=("Arial", 10, "bold")).grid(row=0, column=2, padx=5, pady=5)
password_entry = tk.Entry(top_fields_frame, show="*", width=30, font=("Arial", 10))
password_entry.grid(row=0, column=3, padx=5, pady=5)

main_frame = tk.Frame(root, bg="white")
main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

image_frame = tk.Frame(main_frame, bg="white")
image_frame.pack(fill=tk.BOTH, expand=True)

original_frame = tk.LabelFrame(image_frame, text="Original Image", font=("Arial", 12), bg="white")
original_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

original_img_label = tk.Label(original_frame, bg="white")
original_img_label.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

encrypted_frame = tk.LabelFrame(image_frame, text="Encrypted Image", font=("Arial", 12), bg="white")
encrypted_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

encrypted_img_label = tk.Label(encrypted_frame, bg="white")
encrypted_img_label.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

selected_image = None
END_MARKER = "#####"

def select_image():
    """Opens file dialog to select an image and displays it."""
    global selected_image
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        selected_image = file_path
        display_image(file_path, original_img_label)

def display_image(image_path, label):
    """Displays an image inside a given label."""
    image = Image.open(image_path)
    image = image.resize((350, 350), Image.Resampling.LANCZOS)
    img_tk = ImageTk.PhotoImage(image)
    label.config(image=img_tk)
    label.image = img_tk

def encrypt_image():
    """Encrypts the image and saves it as 'encryptedImage.png'."""
    if not selected_image:
        messagebox.showerror("Error", "Please select an image first!")
        return
    
    img = cv2.imread(selected_image)
    if img is None:
        messagebox.showerror("Error", "Invalid image file!")
        return
    
    user_password = password_entry.get()
    if not user_password:
        messagebox.showerror("Error", "Please enter a password!")
        return
    
    secret_message = secret_msg_entry.get()
    if not secret_message:
        messagebox.showerror("Error", "Please enter a secret message!")
        return

    message = secret_message + END_MARKER
    message_bin = ''.join(format(ord(i), '08b') for i in message)

    data_index = 0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(3):
                if data_index < len(message_bin):
                    img[i, j, k] = (img[i, j, k] & 254) | int(message_bin[data_index])
                    data_index += 1

    cv2.imwrite("encryptedImage.png", img)
    
    show_encrypted_image()
    messagebox.showinfo("Encryption", "Image encrypted successfully!")

def show_encrypted_image():
    """Displays the encrypted image in the right panel."""
    if os.path.exists("encryptedImage.png"):
        display_image("encryptedImage.png", encrypted_img_label)

def decrypt_image():
    """Decrypts the image and retrieves the hidden message."""
    if not os.path.exists("encryptedImage.png"):
        messagebox.showerror("Error", "Encrypted image not found!")
        return

    img = cv2.imread("encryptedImage.png")
    if img is None:
        messagebox.showerror("Error", "Error loading encrypted image!")
        return

    user_password = password_entry.get()
    if not user_password:
        messagebox.showerror("Error", "Please enter a password!")
        return

    msg_bin = ""
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(3):
                msg_bin += str(img[i, j, k] & 1)

    chars = [msg_bin[i:i+8] for i in range(0, len(msg_bin), 8)]
    message = ''.join(chr(int(char, 2)) for char in chars)

    if END_MARKER in message:
        message = message[:message.index(END_MARKER)]  

    messagebox.showinfo("Decryption", f"Decrypted Message: {message}")

# ----- Buttons -----
button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Select Image", command=select_image, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(side=tk.LEFT, padx=10)
tk.Button(button_frame, text="Encrypt", command=encrypt_image, bg="#2196F3", fg="white", font=("Arial", 12)).pack(side=tk.LEFT, padx=10)
tk.Button(button_frame, text="Decrypt", command=decrypt_image, bg="#f44336", fg="white", font=("Arial", 12)).pack(side=tk.LEFT, padx=10)

# Start Tkinter loop
root.mainloop()
