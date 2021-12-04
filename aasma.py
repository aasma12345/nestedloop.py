n=int(input("enter the number: "))
a=0
b=1
sum=0
count=1
print("fibonacci series",end="")
while count<=n:
    print(sum,end="")
    count=count+1
    a=b
    b=sum
    sum=a+b 

num=int(input("enter the number: "))
f=1
i=1
while i<=num:
    f=f*i
    i=i+1
print(f)


num=int(input("enter the number: "))
i=num
sum=0
while num>=0:
    sum=sum+num
    num=num-1
    average=sum/i
print(sum)
print(average)
    


num=int(input("enter the number: "))
temp=num
rev=0
while num>0:
    dig=num%10
    rev=rev*10+dig
    num=num//10
if temp==rev:
    print("the number is palindrome!")
else:
    print("not a palindrome!")


i=1
while  i<=5:
    j=1
    while j<=i:
        print(chr(i+64),end="")
        j=j+1
    print()
    i=i+1


i=1
while i<=7:
    print("*"*i)
    i=i+1


i=0
while i<=5:
    j=0
    while j<=i:
        if j<=i:
            j=j+1
        else:
            j=j-1
        print(j,end="")
    print()
    i=i+1


i=1
while i<=5:
    j=1
    while j<=5:
        if j<=5:
            j=j+1
        else:
            j=j-1
        print(i,end="")
    print()
    i=i+1

i=5
while i>=1:
    j=5
    while j>=1:
        if j>=1:
            j=j-1
        else:
            j=j+1
        print(i,end="")
    print()
    i=i-1


i=1
while  i<=5:
    j=1
    while j<=5:
        print(chr(i+64),end="")
        j=j+1
    print()
    i=i+1                                                                           
  
i=1
while i<=5:
    j=1
    while j<=5:
        if j<=5:
            j=j+1
        else:
            j=j-1
        print(i,end="")
    print("")
    i=i+1



