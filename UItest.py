import tkinter as tk
from tkinter import filedialog
from userInt import reader

def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        x=reader.getAmount(file_path)
        print(x)

window = tk.Tk()
window.title("Upload")

button = tk.Button(window, text="Upload File", command=upload_file)
button.pack(pady=20)

window.mainloop()