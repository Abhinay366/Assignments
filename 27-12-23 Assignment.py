import csv
with open("studentprogressreport.csv","w",newline='') as s:
    w=csv.writer(s)
    w.writerow(["student_name","student_rollno","Maths_marks","English marks","Science_marks","Social_marks","Total_marks","Average_marks","Percentage","Result"])
    n=int(input("enter the number of employee to entry details: "))
    for i in range(1,n+1):
        print(i," STUDENTS MARKS DETAILS ")
        stuname=input("enter name : ")
        sturollno=int(input("enter rollnum :"))
        maths=int(input("enter maths marks :"))
        english=int(input("enter english marks : "))
        science=int(input("enter science marks :"))
        social=int(input("enter social marks:"))
        x=(maths+english+science+social)
        total=x
        y=x/4
        avg=y
        z=x/400*100
        per=z
        result="pass" if per>=35 else "fail"
    
        w.writerow([stuname,sturollno,maths,english,science,social,total,avg,per,result])
    print("total emp data written to csv file ")

f1=open("video.mp4",'rb')
f2=open("new_video.mp4",'wb')
b=f1.read()
f2.write(b)
