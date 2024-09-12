class reader():

    def store(option, filePath):
        file = open(filePath, "r")
        file.readline()
        lineTwo = file.readline()
        if (lineTwo == "ASIN\tProduct Name\tProduct Count\n"):
            return(reader.storeMethod2(option, filePath))
        elif (lineTwo == "ASIN\n"):
            return(reader.storeMethod4(option, filePath))
        else:
            print("Could not read that file. Make sure you are saving the file with Word or WordPad")

    def storeMethod2(option, filePath):
        file = open(filePath, "r")
        asinNum = []
        quantity = []
        line = file.readline()
        length = 1
        #Gets how many lines are in the txt file
        while (line != ""):
            line = file.readline()
            length += 1
        file.close()  
        readFile = open(filePath, "r")
        #Skips the first two unneeded lines
        readFile.readline()
        readFile.readline()
        count = 0
        while (count < length):
            line = readFile.readline()
            if (len(line) != 1 and len(line) != 0):
                if (line[len(line) - 3] != "\t"):
                    if (line[len(line) - 5] == "\t"):
                        quantity.append(line[len(line) - 4] + line[len(line) - 3] + line[len(line) - 2])
                        asinNum.append(line[0:10])
                    else:
                        quantity.append(line[len(line) - 3] + line[len(line) - 2])
                        asinNum.append(line[0:10])
                else:
                    quantity.append(line[len(line) - 2])
                    asinNum.append(line[0:10])
            count += 1
        readFile.close()
        if (option == "ASIN"):
            return asinNum
        else:
            return quantity      


    def storeMethod4(option, filePath):
        file = open(filePath, "r")
        asinNum = []
        quantity = []
        line = file.readline()
        length = 1
        #Gets how many lines are in the txt file
        while (line != "AMAZON CONFIDENTIAL\n"):
            line = file.readline()
            length += 1
        file.close()
        #Only counts the lines that we want
        length -= 7
        readFile = open(filePath, "r")
        #Skips the first four unneeded lines
        readFile.readline()
        readFile.readline()
        readFile.readline()
        readFile.readline()
        count = 0
        #Gets the ASIN numbers and quantities and puts them into lists while remvoing the \n on the end
        while (count < length/3):
            asinNum.append(readFile.readline())
            asinNum[count] = asinNum[count].replace("\n", "")
            readFile.readline()
            quantity.append(readFile.readline())
            quantity[count] = quantity[count].replace("\n", "")
            count += 1
        readFile.close()
        if (option == "ASIN"):
            return asinNum
        else:
            return quantity
