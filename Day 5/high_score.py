# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
# Important you are not allowed to use the max or min functions. The output words must match the example

high_score = 0
for i in student_scores:
  if i > high_score:
    high_score = i

print(f"The highest score in the class is: {high_score}")