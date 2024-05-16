student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.

student_grades = {
}

# TODO-2: Write your code below to add the grades to student_grades.👇

for i in student_scores:
      if student_scores[i] > 90:
            student_grades[i] = "Outstanding"
      
      elif student_scores[i] in range(81, 90):
            student_grades[i] = "Exceeds Expectations"
      
      elif student_scores[i] in range(71, 80):
            student_grades[i] = "Acceptable"

      else:
            student_grades[i] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)