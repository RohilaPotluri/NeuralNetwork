#Input string from console
sentence = input("Enter your sentence ")

#Creating an empty list
senList = []
#Assigning each word it's value
senList = sentence.split(" ")

newList = []

# checking the sentence if it has any values like "python" and replacing it with "pythons"
i = 0
while i < len(senList):
    if senList[i] == "python":
        newList.append("pythons")
    else:
        newList.append(senList[i])
    i = i + 1

# changes list back to a string
strSen = ""
for i in newList:
    strSen = strSen + i + " "

print(strSen)
