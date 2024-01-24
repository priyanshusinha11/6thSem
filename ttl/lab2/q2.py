#grade of a student

print("Enter the marks obtained by a student in CN, SE, HPC, DAA, AI and BD")
cn = int(input())
se = int(input())
hpc = int(input())
daa = int(input())
ai = int(input())
bd = int(input())

avgMarks = (cn+se+hpc+daa+ai+bd)/6.0
if avgMarks>100:
    print("Wrong input")
elif avgMarks>=90:
    print("Grade: O")
elif avgMarks>=80 and avgMarks<90:
    print("Grade: E")
elif avgMarks>=70 and avgMarks<80:
    print("Grade: A")
elif avgMarks>=60 and avgMarks<70:
    print("Grade: B")
elif avgMarks>=50 and avgMarks<60:
    print("Grade: C")
elif avgMarks>=40 and avgMarks<50:
    print("Grade: D")
else:
    print("Fail!")
