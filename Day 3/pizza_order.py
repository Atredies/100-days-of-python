print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

if size == 'S':
  price = 15

if size == 'M':
  price = 20

if size == 'L':
  price = 25

if add_pepperoni == 'Y':
  pepperoni = 2

else:
  pepperoni = 0

if extra_cheese == 'Y':
  cheese = 1
  
else:
  cheese = 0

final_price = price + pepperoni + cheese

print(f"Your final bill is: ${final_price}.")