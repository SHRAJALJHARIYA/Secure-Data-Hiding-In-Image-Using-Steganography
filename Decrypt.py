
import numpy as np
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
        # Load image using NumPy for better performance
        img = Image.open(image_path)
        img_array = np.array(img)

        # Extract LSBs from the red channel
        r_channel = img_array[:, :, 0]  # Extract red channel
        binary_message = np.unpackbits(r_channel).astype(str)  # Get LSBs
        binary_message = "".join(binary_message[7::8])  # Take LSBs only
        
        # Convert binary to text and stop early
        chars = []
        for i in range(0, len(binary_message), 8):
            char_bin = binary_message[i:i+8]
            char = chr(int(char_bin, 2))
            if char == "#":  # Stop when delimiter starts
                if "".join(chars[-2:]) == "##":  
                    break
            chars.append(char)

        extracted_text = "".join(chars[:-2])  # Remove end marker

        messagebox.showinfo("Decrypted Message", extracted_text)

    except Exception as e:
        messagebox.showerror("Error", str(e))
