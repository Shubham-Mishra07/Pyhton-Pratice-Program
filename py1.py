#swapping of two numbers without using third variable
a=5
b=2
a=a+b
b=a-b
a=a-b
print (a,b)


# fruits=["Apple","Banana","Orange"]
# str="python"
# for i in fruits:
#     print(i, end=" ")
# for i in str:
#     print(i,end=" ")
#     if i=="h":
#         continue
#     print(i)
#for i in range(1,25,2):
 #   print(i)

#print table of given number using for loop
number=int(input("enter the number "))
for i in range(1,11): 
    print (number,'x',i,'==',number*i)
    
# 4 3 2 1 
# 3 2 1
# 2 1 
# 1
number=int(input("enter the number "))
for i in range(number,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
    j=i
print()

# 1
# 1 2 
# 1 2 3 
number=int(input("enter two numbers"))
for i in range(number+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n")


# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
number=int(input("enter two numbers"))
for i in range(0,number+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print(" ")
for i in range(number-1,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print(" ")


#COUNT OF DIGITS IN A NUMBER
n=int(input("Enter the number"))
num=n
count=0
while n>0:
    n=n//10
    count +=1
    
print("count =",count)

#SUM OF DIGITS
n=int(input("Enter the number"))
sum=0
while n>0:
    remainder=n%10
    sum =sum+remainder
    n=n//10
print("sum of the digits =",sum)

#REVERSE THE NUMBER
n=int(input("Enter the number"))
rev=0
while n>0:
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("reverse of the digits =",rev)


#REVERSE THE STRING
str=input("Enter")
s1=str[::-1]
print(s1)


#TO CHECK IF TWO STRINGS ARE PALLINDROME
str=input("Enter")
s1=str[::-1]
if (str==s1):
    print("pallindrome")
else:
    print("not pallindrome")

# NUMBER OF VOWELS PRESENT IN THE WORD
string=input("enter string")
vowels=0
for i in string:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vowels=vowels+1
print("vowels are",vowels)

# ARMSTRONG NUMBER
min=100
max=999
for i in range(min,max+1):
    sum=0
    temp=i
    while temp>0:
        digit=temp%10
        sum=sum+ digit ** 3
        temp//=10
    
    if i==sum:
        print(i)

    
#FUNCTION
def Even_Odd(number):
    if number%2==0:
        print("Even")
    else:
        print ("odd")
    
Even_Odd(45)



#LARGEST OF THREE NUMBER
def largest(num1,num2,num3):
    if(num1>num2):
        print("num1 is greater:",num1)
    elif(num2>num3):
        print("num2 is greater:",num2)
    else:
        print("num3 is greater:",num3)
largest(45,45,33)

#SUM OF DIGITS 
def add(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum
print(add(3,4,7,8))
add(3,4,7,8)

