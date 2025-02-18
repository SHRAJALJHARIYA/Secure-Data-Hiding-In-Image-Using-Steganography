from tkinter import filedialog, messagebox
from PIL import Image
import os

def upload_image_encrypt(entry_image_encrypt, show_preview, image_preview_encrypt):
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if file_path:
        entry_image_encrypt.delete(0, "end")
        entry_image_encrypt.insert(0, file_path)
        show_preview(image_preview_encrypt, file_path)

def encrypt_message(entry_image_encrypt, entry_message_encrypt, entry_key_encrypt):
    image_path = entry_image_encrypt.get()
    message = entry_message_encrypt.get()
    key = entry_key_encrypt.get()
    if not image_path or not message or not key:
        messagebox.showerror("Error", "All fields are required!")
        return
    
    try:
        img = Image.open(image_path)
        encoded = img.copy()
        width, height = img.size
        binary_message = ''.join(format(ord(c), '08b') for c in (message + '###'))
        data_index = 0

        for y in range(height):
            for x in range(width):
                if data_index < len(binary_message):
                    r, g, b = img.getpixel((x, y))
                    r = (r & ~1) | int(binary_message[data_index])
                    encoded.putpixel((x, y), (r, g, b))
                    data_index += 1
                else:
                    break

        output_path = os.path.splitext(image_path)[0] + "_encoded.png"
        encoded.save(output_path)
        messagebox.showinfo("Success", f"Message encrypted and saved as {output_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))
