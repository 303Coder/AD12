import PriceAPI
from reader import reader
import reader2
import time

import tkinter as tk
from tkinter import filedialog








Price = 0








# Initialize Tkninter Window
App = tk.Tk()

#Name Window
App.title("Total Donation Count")

# Set the window size
App.geometry("440x300")

# Prevent resizing
App.resizable(False, False)

# Title
Title = tk.Label(App, text="AD12 Inventory Price Calculator", font=("Arial", 20, "bold"))
Title.pack(anchor="center")


#Blank Space for spacing
Title = tk.Label(App, text="", font=("Arial", 100, "bold"))
Title.pack()





def upload_file():
    file_path = filedialog.askopenfilename()
    print(file_path)



    global ASIN 
    ASIN = reader2.getAsin(file_path)
    global Quantity
    Quantity = reader2.getAmount(file_path)
    global count
    count = 0



    Title = tk.Label(App, text=f"{count} of {len(ASIN)}'s found")
    Title.pack()

    def totalPrice(a, b):
        totalPrice = 0
        count = 0
        for x in range(len(a)):
            totalPrice += PriceAPI.find(a[x]) * int(b[x])
            count+=1
            time.sleep(1)

            
            
        return totalPrice
    
    totalPrice = totalPrice(ASIN[:2], Quantity[:2])

    Price = totalPrice



#Create and add "Upload File" Button
button = tk.Button(App, text="Upload File", command=upload_file)
button.pack()



lbl = tk.Label(App, text=f"Total Inventory Price: ${Price}")
lbl.pack()

App.mainloop()


    


