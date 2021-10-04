#Challange4 Week 1

mass = float(input("Enter water mass: "))
temp = int(input("Enter temperature change: "))
specific_heat = 4186 # jouls - water

heat_transfer = mass * specific_heat * temp

print(heat_transfer, "joules")


kilowatt = (heat_transfer * (1/3600000))
print(round(kilowatt, 2), "kilowatt hours")

energy_cost = 8.9

bill = round(kilowatt * energy_cost, 2)

print(bill, "pence")



