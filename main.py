import customtkinter
from PIL import Image, ImageTk
from Encrypt import upload_image_encrypt, encrypt_message
from Decrypt import upload_image_decrypt, decrypt_message

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("500x600")
root.iconbitmap("logo.ico")
root.title("Secure Data Hiding In Image Using Stegnography")

tabview = customtkinter.CTkTabview(master=root, width=400, height=500)
tabview.pack(padx=20, pady=20)

frame1 = tabview.add("Encryption")
frame2 = tabview.add("Decryption")

# Encryption UI
frame_encrypt = customtkinter.CTkFrame(master=frame1)
frame_encrypt.pack(pady=20, padx=10, expand=True, fill="both")

entry_image_encrypt = customtkinter.CTkEntry(master=frame_encrypt, placeholder_text="Image Address")
entry_image_encrypt.pack(pady=5, padx=10)

btn_upload_encrypt = customtkinter.CTkButton(frame_encrypt, text="Upload Image",command=lambda: upload_image_encrypt(entry_image_encrypt, show_preview, image_preview_encrypt))
btn_upload_encrypt.pack(pady=5)

image_preview_encrypt = customtkinter.CTkLabel(frame_encrypt, text="")
image_preview_encrypt.pack(pady=5)

entry_message_encrypt = customtkinter.CTkEntry(master=frame_encrypt, placeholder_text="Enter secret message")
entry_message_encrypt.pack(pady=5, padx=10)

entry_key_encrypt = customtkinter.CTkEntry(master=frame_encrypt, placeholder_text="Enter secret key")
entry_key_encrypt.pack(pady=5, padx=10)

btn_encrypt = customtkinter.CTkButton(frame_encrypt, text="Encrypt",command=lambda: encrypt_message(entry_image_encrypt, entry_message_encrypt, entry_key_encrypt))
btn_encrypt.pack(pady=10)

# Decryption UI
frame_decrypt = customtkinter.CTkFrame(master=frame2)
frame_decrypt.pack(pady=20, padx=10, expand=True, fill="both")

entry_image_decrypt = customtkinter.CTkEntry(master=frame_decrypt, placeholder_text="Image Address")
entry_image_decrypt.pack(pady=5, padx=10)

btn_upload_decrypt = customtkinter.CTkButton(frame_decrypt, text="Upload Image",command=lambda: upload_image_decrypt(entry_image_decrypt, show_preview, image_preview_decrypt))
btn_upload_decrypt.pack(pady=5)

image_preview_decrypt = customtkinter.CTkLabel(frame_decrypt, text="")
image_preview_decrypt.pack(pady=5)

entry_key_decrypt = customtkinter.CTkEntry(master=frame_decrypt, placeholder_text="Enter secret key")
entry_key_decrypt.pack(pady=5, padx=10)

btn_decrypt = customtkinter.CTkButton(frame_decrypt, text="Decrypt",command=lambda: decrypt_message(entry_image_decrypt, entry_key_decrypt))
btn_decrypt.pack(pady=10)

# Image preview function
def show_preview(label, file_path):
    img = Image.open(file_path)
    img = img.resize((100, 100))

    # Convert to CTkImage instead of ImageTk.PhotoImage
    ctk_image = customtkinter.CTkImage(light_image=img, size=(200, 200))

    label.configure(image=ctk_image)
    label.image = ctk_image  # Keep reference to prevent garbage collection

copyright_label = customtkinter.CTkLabel(
    root,text="© 2024 Shrajal. All rights reserved.",font=("Arial", 10)
)
copyright_label.pack(side="bottom", pady=5)



root.mainloop()
