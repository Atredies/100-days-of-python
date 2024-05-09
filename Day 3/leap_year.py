# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 == 0 and year % 400 == 5:
  print("Leap year")

else:
  print("Not leap year")