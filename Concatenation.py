#Concatenation of two Strings
str1=input("Enter the frist name :")
str2=input("Enter the Second name :")

str3=str1+""+str2

print("The Concatenation of names are :", str3)

#another example
a="Virat"
b="Kohil"
c=a+""+b
print("Full name :",c)

#accessing the sub string
start_index=5
end_index=8
substring=c[start_index:end_index]

#printing Substring
print("SubString : ",substring)
