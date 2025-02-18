from tkinter import filedialog, messagebox
from PIL import Image

def upload_image_decrypt(entry_image_decrypt, show_preview, image_preview_decrypt):
    file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    if file_path:
        entry_image_decrypt.delete(0, "end")
        entry_image_decrypt.insert(0, file_path)
        show_preview(image_preview_decrypt, file_path)

def decrypt_message(entry_image_decrypt, entry_key_decrypt):
    image_path = entry_image_decrypt.get()
    key = entry_key_decrypt.get()
    if not image_path or not key:
        messagebox.showerror("Error", "All fields are required!")
        return
    
    try:
        img = Image.open(image_path)
        width, height = img.size
        binary_message = ""

        for y in range(height):
            for x in range(width):
                r, g, b = img.getpixel((x, y))
                binary_message += str(r & 1)

        decoded_chars = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
        extracted_text = "".join([chr(int(b, 2)) for b in decoded_chars])
        extracted_text = extracted_text.split("###")[0]

        messagebox.showinfo("Decrypted Message", extracted_text)
    except Exception as e:
        messagebox.showerror("Error", str(e))
