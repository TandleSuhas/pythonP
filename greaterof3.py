a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
c=int(input("Enter the third number :"))

greater="The three numbers are {} , {} and {}"
print(greater.format(a,b,c))

if(a>b and a>c):
    print("a is greater !")
elif(b>a and b>c) :
    print("b is graeter !")
else:
    print("c is graeter !")    
