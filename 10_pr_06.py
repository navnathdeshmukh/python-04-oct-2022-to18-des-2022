#Q. write  a programe   to lculate  the grade  of  astudent  from  his  marks  from  following  sheme :
#90-100-ex
#80-90-A
#70-60-B
#60-50-c
#<50-F

marks = int(input("Enter Your Marks\n"))

if marks>=90:
    grade = "Ex"
elif marks>=80:
    grade = "A"
elif marks>=70:
    grade = "B"
elif marks>=60:
    grade = "C"
elif marks>=50:
    grade = "D" 
else:
    grade = "F"

print("Your grade is " + grade)