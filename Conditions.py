"""
age= int(input("Enter the age:"))
if(age>=18):
    print("We can apply for a license")
elif(age>=16 and age<18):
    print("Learning License can be applied")
else:
    print("Not")

num=int(input("Enter the Number:"))

if(num>2 and num<4):
    print("Number is greater than 2")
elif(num>4):
    print("Number is greater than 4")
else:
    print("Number is smaller than 2")
"""
marks=int(input("Marks:"))
if(marks>=90):
    grade="A" #indentation:proper spacing only in python
elif(marks>=80 and marks<90):
    grade="B" #indentation:proper spacing only in python
elif(marks>=70 and marks<80):
    grade="C" #indentation:proper spacing only in python
else:
    grade="D" #indentation:proper spacing only in python

print("Grade of the Student->",grade)