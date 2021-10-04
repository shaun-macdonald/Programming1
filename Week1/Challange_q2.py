#Challaneg_q2.py Week1

days = int(input("Input days "))
hours = int(input("Input hours "))
minutes = int(input("Input minutes "))
seconds = int(input("Input seconds "))

dayscalc = ((days*24) * (3600))
print(dayscalc)

hourscalc = (hours * 3600)
minutescalc = (minutes * 60)
secondscalc = seconds
finalcalc = dayscalc + hourscalc + minutescalc + secondscalc

print("Total seconds in duration is: ", finalcalc)

