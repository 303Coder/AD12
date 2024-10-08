import tkinter as tk
from tkinter import filedialog



def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        x="total price"
        lbl = tk.Label(DonApp, text=x)
        lbl.grid()

DonApp = tk.Tk()
DonApp.title("Total Donation Count")

button = tk.Button(DonApp, text="Upload File", command=upload_file)
button.grid()

DonApp.mainloop()
