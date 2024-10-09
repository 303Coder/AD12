import PriceAPI
from reader import reader
import reader2
import time

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog








# Initialize Tkninter Window
App = tk.Tk()

#Name Window
App.title("Total Donation Count")

# Set the window size
App.geometry("440x300")

# Prevent resizing
#App.resizable(False, False)

# Title
Title = tk.Label(App, text="AD12 Inventory Price Calculator", font=("Arial", 20, "bold"))
Title.pack(anchor="center")

#Blank Space for spacing
blankSpace = tk.Label(App, text="", font=("Arial", 30, "bold"))
blankSpace.pack()






# Label for the file opened --- "File: FILE_PATH"
lbl1 = tk.Label(App, text=f"File: ''")
lbl1.pack()

# Label "Findind total price"
lbl2 = tk.Label(App, text=f"")
lbl2.pack()


# Label stating # of ASINs found
lbl3 = tk.Label(App, text=f"")
lbl3.pack()


# Label with total inventory price
lbl4 = tk.Label(App, text=f"")
lbl4.pack()



Price = 0
Count = 0
file_path = ""
ASIN = []
Quantity = []




def prices():
    # Count variable for # of ASINs found 
    global count
    count = 0

    global Price
    Price = 0

    lbl3.config(text=f"{count} of {len(ASIN)} ASIN's found")



    for x in range(len(ASIN)):
        currentPrice = PriceAPI.find(ASIN[x]) * int(Quantity[x]) 
        Price += currentPrice
        count+=1
        lbl3.config(text=f"{count} of {len(ASIN)} ASIN's found")
        lbl4.config(text=f"Total Inventory Price: ${Price}")
        time.sleep(1)

        file = open("Data.txt", "w")
        file.write(f"{ASIN[x]} \t {currentPrice} \t {Quantity[x]}\n")

    file.close()

        
        






def lists():
    # Creats ASIN var and gets the ASINs from doc
    global ASIN 
    ASIN = reader2.getAsin(file_path)


    # Creats Quantity var and gets the Quantities from doc
    global Quantity
    Quantity = reader2.getAmount(file_path)

    lbl3.config(text=f"Finding total Price, please Wait. This may take a while...")





def upload_file():
    #Open and sets file path to variable
    global file_path
    file_path = filedialog.askopenfilename()
    #print(file_path)

    lbl1.config(text=f"File: '{file_path}'")

    file = open("Data.txt", "w")
    file.write("ASIN \t Price \t Quantity\n")






def main():
    upload_file()
    lists()
    print(ASIN)
    print(Quantity)
    prices()

            
            





#Create and add "Upload File" Button
button = tk.Button(App, text="Upload File", command=main)
button.pack()


App.mainloop()
