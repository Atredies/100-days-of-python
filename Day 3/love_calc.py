print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

all_name = str(name1) + str(name2)

check_true = 0
for i in all_name.upper():
  if i in ['T', 'R', 'U', 'E']:
    check_true += 1

check_love = 0
for i in all_name.upper():
  if i in ['L', 'O', 'V', 'E']:
    check_love += 1

love_score = str(check_true) + str(check_love)

if int(love_score) < 10 or int(love_score) > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")

elif int(love_score) < 40 or int(love_score) >= 50:
  print(f"Your score is {love_score}, you are alright together.")

else:
  print(f"Your score is {love_score}.")