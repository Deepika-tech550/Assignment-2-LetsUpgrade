#1.Use IF ELSE and ELIF to write a program in python for your Report Cards.
#GRADE -A,B,C,D,EFail
print("REPORT CARD")
print("*********************")
m=int(input("Enter Percentage  Mark"))
if(m>90):
    print("GRADE A")
elif(m>=80 and m<90):
    print("GRADE B")
elif(m>=70 and m<80):
    print("GRADE C")
elif(m>=60 and m<70):
    print("GRADE D")
elif(m>=50 and m<60):
    print("GRADE E")
else:
    print("FAIL")
print("*********************")
#2.Use For Loop to Print Prime Numbers in between 1 to 11

for i in range(1,11):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count=count+1
    if(count==2):
        print(i)

        
#3.Write a program for printing the tables from 1,10 using Nested For Loop


for j in range(1,11):
    
    for i in range(1,11):
        print(i*j)
    print("%d table is stoped" %(j))    
    print("****************")   
#4.Write a program to Print X Prime Numbers using While Loop starting from 0, and take the INput of X from
#the user

print("Python Program to find Prime Number")
 
Number = int(input(" Please Enter any Number: "))
count = 0
i = 2

while(i <= Number//2):
    if(Number % i == 0):
        count = count + 1
        break
    i = i + 1

if (count == 0 and Number != 1):
    print(" %d is a Prime Number" %Number)
else:
    print(" %d is not a Prime Number" %Number)

            
        
    
