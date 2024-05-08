# Remember PEMDASLR (Parentheses, Exponents, Multiply & Divide, Add & Subtract, Left to Right)

print("Wellcome to the tip calculator!")

bill_total = input("What was the total bill? $")
tip_percent = input("How much tip would you like to give? 10, 12, or 15?")
people = input("How many people tto split the bill? ")

total_payment = (float(bill_total) + (float(bill_total) / 100 * float(tip_percent))) / int(people)

print("Each person should pay: $" + str(round(total_payment, 2)))
