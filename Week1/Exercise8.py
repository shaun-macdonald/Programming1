#Exercise 8 Week 1

feet = int(input("Please enter your height in whole feet: "))
inches = int (input("Please enter your the remaining inches of your height: "))

feet_to_inch = feet * 12
height_inches = feet_to_inch + inches
conversion = height_inches * 2.54

print("Your height is {}cm".format(conversion))
