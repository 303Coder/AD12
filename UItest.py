import tkinter as tk
from tkinter import filedialog

def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        print('pressed')

DonApp = tk.Tk()
DonApp.title("Total Donation Count")
lbl = tk.Label(DonApp, text="Donation count")
lbl
button = tk.Button(DonApp, text="Upload File", command=upload_file)
button.pack(expand=1)

DonApp.mainloop()
