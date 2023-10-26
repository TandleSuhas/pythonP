l=input("Enter the Length :")
b=input("Enter the breath :")
dimensions="The length and breath are {} an {}"
print(dimensions.format(l,b))

if(l== b) :
    print("Its is \'SQUARE'")
    area=int(l)*int(b)
    print("The area of sqaure is : ",area)

else :
    print("its is \'RECTANGLE'")
