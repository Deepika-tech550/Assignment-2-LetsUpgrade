#Write down a program in Python for Opening a File and Writing " I Love LetsUpgrade" And close
#it, and read it back again, and then append some data to it and close it.


#1.
a=open("lets.txt",'w')
a.write("I Love LetsUpgrade\n")
a.close()

#2.
b=open("lets.txt",'r')

print(b.read())
b.close()


#3.
c=open("lets.txt",'a+')
c.write("I am from Tamil Nadu\n")
c.write("Nice to see u ")
c.close()


#Write a function which can return a Factorial of any numbers as INT, given in the argument.

def fact(n):
    if(n==0):
        return 1
    return n*fact(n-1)

result=fact(5)
print(result)


