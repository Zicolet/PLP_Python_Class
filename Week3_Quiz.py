'''
1.	Write a simple python programme that can rate students performance as follows;
  a.	Above 80 = distinction
  b.	60 - 70 = credit
  c.	40 - 50 = fair
  d.	Below 40 = fail
'''
# Task 1

isContinue = True
while isContinue:
  student_score = int(input(" Enter student's score: "))

  if student_score >75:
    grade = "Distinction"
    print("\n Student's grade is a",grade )
  elif 55< student_score <= 75:
    grade = "credit"
    print("\n Student's grade is a",grade )
  elif  40 <= student_score <= 55:
    grade = "Fair"
    print("\n Student's grade is a",grade )
  else:
    grade = "Fail"
    print("\n Student's grade is a",grade )

  isContinue = int(input('\n Will you like to Grade another student ? \n 0=> No (To use calculator) | Any other number=> Yes:   '))



'''
2.	Create a simple calculator using python that can perform the following operations;
  a.	Add 2 numbers
  b.	Multiplication
  c.	Division
  d.	Subtraction
'''
print('\n ***** YOU ARE NOW IN CALCULATOR MODE ***** \n')
def calculator(A,B,Y):
  match (Y):
    case "1": return A + B
    case "2": return A * B
    case "3": return A / B
    case "4": return A - B
    case _: return "Error: You have just entered an invalid mathematical operation"


isContinue = True     # Re-assign isContinue to enter calculator loop
while isContinue:

  Operation = input('\n Which operation will you like to perform \n 1=> Addition | 2=> Multiplication | 3=> Division | 4=> Substraction :   ')
  Operand_1 = int(input("\n  Enter first operand: "))
  Operand_2 = int(input(" Enter second operand: "))
  print('\n Answer is :',calculator(Operand_1, Operand_2,Operation))
  
  isContinue = int(input('Will you like to perform another operation ? \n 0=> No | Any other number=> Yes:   '))

print("\n  Thank You for Using My First Python Calculator, GOD BLESS !!! ")







    