import webScrapper
from reader import reader
from datetime import datetime
import time



# path = "D:\Data.txt"


# ASIN = reader.store("ASIN", path)
# Quantity = reader.store("Quantity", path)

ASIN = ["B00000J0S3", "B00004YV1W", "B00005BZRZ", "B00005BZRZ", "B000067NXE"]
Quantity = ["1", "4", "1", "1", "1"]

Total = 0

count = 0

startTime = datetime.now()

for item in ASIN:
    webScrapper.initialize(item)
    price = webScrapper.find()

    if price != None:
        length = len(price)
        price = price[1:length]
        price = float(price)

        Q = int(Quantity[count])
        Total += price * Q
    
    #print(count)
    count += 1

endTime = datetime.now()


print("$" + str(Total))
print(webScrapper.returnErrors())
print(endTime-startTime)



x = open("Efficiency.txt", "a")
x.write(f"\n ${str(Total)} \n {webScrapper.returnErrors} \n {endTime-startTime}")
x.close()