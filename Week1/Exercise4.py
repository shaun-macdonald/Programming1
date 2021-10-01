#Exercise 4 Week 1

salary = int(input("Please enter youre yearly salary "))
pre_tax = salary / 12
tax_rate = 0.2
post_tax = (salary * 0.8 ) / 12

print("Salary before tax:",format(pre_tax, '.2f'))
print("Salary after tax:", format(post_tax, '.2f'))