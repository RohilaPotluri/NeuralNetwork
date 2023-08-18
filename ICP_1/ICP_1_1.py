
# Take input string from the console
string = input("Enter the string ")

# Empty string list
strList = []

# To fill the list with individual characters
strList[:0] = string
print("String list:", strList)

# Deleting atleast two characters
strList.pop(2)
strList.pop(3)

# Reversing the list
strList.reverse()

#A blank string initially, then iterating through strList
final_string = ""
for i in strList:
    final_string = final_string + i

# Final string
print(final_string)


# Taking inputs
x = int(input("Enter the first number "))
y = int(input("Enter the second number "))


# operations for +-/* are done in the print statements

print(x, "+", y, "=", x+y)
print(x, "-", y, "=", x-y)
print(x, "*", y, "=", x*y)
print(x, "/", y, "=", x/y)
