#Exercise 7 Week 1

time = int(input("Please enter a time in seconds: "))
c = 3*pow(10, 8)
distance = c * time
meters = distance
kilometers = distance / 1000
miles = kilometers * 0.6213

print("Distance travelled in meterts is {}m, in kilometers is {}km and in miles is {} miles".format(meters, kilometers, miles))