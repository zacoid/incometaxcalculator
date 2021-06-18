income = float(input("Enter your taxable income: $"))

tax = 0.0
if income <= 9950:
    tax = income * .10
elif income <= 40525:
    tax = 995 + (.12 *(income-9950))
elif income <= 86375:
    tax = 4664 + (.22*(income-40525))
elif income <= 164925:
    tax = 14751 +(.24*(income-86375))
elif income <= 209425:
    tax = 33603 +(.32*(income-164925))
elif income <= 523600:
    tax = 47843 +(.35*(income-209425))
else:
    tax = 157804.25 +(.37*(income-523600))

remainder = income - tax

print("You will pay ${tax}".format(tax = tax), "in income tax\n")

print("You have ${rem}".format(rem = remainder), "left\n")