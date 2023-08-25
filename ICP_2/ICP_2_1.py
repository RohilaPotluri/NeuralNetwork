# taking first and last names from console
First_name=input("Enter your first name:")
Last_name=input("Enter your last name:")
Full_name= First_name + " "  +Last_name # string concatenation
print("Your full name :" + Full_name)



str = Full_name
def string_alernative(str):
    new_str=""
    for index,char in enumerate (str): # enumerating the string
        if index % 2 == 0: # %2 for taking every other character
            new_str += char #appending to the output
    return new_str

alt_name = string_alernative(str) #altered name
print("Alternative name is: " +alt_name)