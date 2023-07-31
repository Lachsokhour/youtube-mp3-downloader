import youtube_dl
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def download_audio():
    link = entry_link.get()
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'outtmpl': f"{file_path.get()}/%(title)s.%(ext)s",
    }

    # Disable the download button during the download process
    btn_download.config(state=tk.DISABLED)
    progress_label.config(text="Downloading...")

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

    # Enable the download button after the download completes
    btn_download.config(state=tk.NORMAL)
    progress_label.config(text="Download completed successfully!")
    # Clear the entry_link after download success
    entry_link.delete(0, tk.END)
    # Schedule the label to be cleared after 3 seconds (3000 milliseconds)
    root.after(3000, clear_success_message)

def clear_success_message():
    progress_label.config(text="")

def browse_folder():
    folder_path = filedialog.askdirectory()
    file_path.set(folder_path)

# GUI setup
root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("700x500")  # Set the initial size of the window (width x height)

file_path = tk.StringVar()

# Load the logo image using Pillow and resize it to a smaller size
logo_image = Image.open("mp3.png")  # Replace "your_logo.png" with the actual image file name or path
logo_image = logo_image.resize((90, 90))  # Replace 100x100 with the desired width and height

# Convert the resized image to a PhotoImage object
logo_image = ImageTk.PhotoImage(logo_image)

# Create a Label widget to display the logo
logo_label = tk.Label(root, image=logo_image)
logo_label.pack()

label_link = tk.Label(root, text="Please enter your YouTube video link:", font=("Arial", 14), bd=2)
label_link.pack(pady=5)  # Add padding at the top

entry_link = tk.Entry(root, width=40, font=("Arial", 12), bd=1)  # Adjust the width, add height and border thickness
entry_link.pack(ipady=10, pady=5)  # Add internal and external padding

label_save = tk.Label(root, font=("Arial", 12), text="Save location:")
label_save.pack(pady=5)  # Add padding between the label and entry box

entry_save = tk.Entry(root, textvariable=file_path, width=40, font=("Arial", 12), bd=1)  # Adjust the width, add height and border thickness
entry_save.pack(ipady=10, pady=5)  # Add internal and external padding

btn_browse = tk.Button(root, text="Browse", width=10, command=browse_folder)  # Adjust the width of the button
btn_browse.pack(pady=5)  # Add padding between the entry box and button

btn_download = tk.Button(root, text="Download Audio", width=20, height=2, command=download_audio)  # Adjust the width and height of the button
btn_download.pack(pady=5)  # Add padding at the bottom

# Label to display progress or success message
progress_label = tk.Label(root, fg="green")
progress_label.pack()

# Add a label at the left bottom
left_bottom_label = tk.Label(root,fg="red", text="Copyright: LACH Sokhour", font=("Arial", 11))
left_bottom_label.pack(side=tk.RIGHT, padx=10, pady=10, anchor=tk.SW)

root.mainloop()
