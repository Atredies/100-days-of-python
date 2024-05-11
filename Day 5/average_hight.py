# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇

total_hight = 0
total_len = 0
for i in student_heights:
  total_hight += i
  total_len += 1

total = total_hight / total_len

print(round(total))