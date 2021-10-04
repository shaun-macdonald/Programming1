

amount = int(input("Enter change amount: "))
total = int(amount)


coin1 = 1
coin2 = 2
coin5 = 5
coin10 = 10
coin20 = 20
coin50 = 50
coin100 = 100
coin200 = 200

two_pound1 = amount // coin200
two_pound2 = amount % coin200

pound1 = two_pound2 // coin100
pound2 = two_pound2 % coin100

fifty1 = pound2 // coin50
fifty2 = pound2 % coin50

twenty1 = fifty2 // coin20
twenty2 = fifty2 % coin20

ten1 = twenty2 // coin10
ten2 = twenty2 % coin10

five1 = ten2 // coin5
five2 = ten2 % coin5

two1 = five2 // coin2
two2 = five2 % coin2

one1 = two2 // coin1
one2 = two2 % coin1



print("Your change is: \n {} 2 pound coin \n {} 1 pound coin \n {} 50p \n {} 20p \n {} 10p \n {} 5p \n {} 2p \n {} 1p".format(two_pound1, pound1, fifty1, twenty1, ten1, five1, two1, one1))