height_inch = []
customers = int(input("Enter the no of customers: "))
for i in range(customers):
    height_ins = float(input("Enter the customers height ".format(i+1)))
    height_inch.append(height_ins)

height_cm=[i*2.54 for i in height_inch]
print("height in inches",height_inch)
print("height in centimeters",height_cm)