import docx2txt as d2t

def getAsin(path):

    asinNum=[]
    #sets the words from the docx file to the variable doc
    doc=d2t.process(path)
    num=0
    #goes through all the characters in variable doc to check if there is "\n" followed up by "B0" and appends the next 10 charecters to the list asinNum
    for x in doc:
        x = doc[num:num+2]
        if x=='B0' and doc[num-1:num]=='\n':
            asinNum.append(doc[num:num+10])
        num+=1
    return asinNum




def getAmount(path):
    # goes through all the characters in variable doc to check if there is "\n" followed by string of numbers which ends with "\n" and adds the number to the list amountNum
    amountNum=[]
    num=0
    #sets the words from the docx file to the variable doc
    doc=d2t.process(path)
    for z in doc:
        if z.isnumeric() and doc[num-1:num] == '\n':
            num2=num
            num3=num
            while doc[num2+1:num3+2]!='\n' and doc[num2+1:num3+2].isnumeric():
                num2+=1
                num3+=1
            if doc[num2+1:num3+2] == '\n':
                amountNum.append(doc[num:num2+1])    
        num+=1
    amountNum.append(doc[len(doc)-1])
    return amountNum