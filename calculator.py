# nestedloop.py
print("1 addition")
print("2 subtraction")
print("3 multiplication")
print("4 division")

choise=input("enter your choise: ")
num1=int(input("enter num1: "))
num2=int(input("enter num2: "))

if choise=="1":
    print(num1,"+",num2,"=",(num1+num2))
elif choise=="2":
    print(num1,"-",num2,"=",(num1-num2))
elif choise=="3":
    print(num1,"*",num2,"=",(num1*num2))
elif choise=="4":
    if num2==0.0:
        print("divide by 0 error")
    else:
        print(num1,"/",num2,"=",(num1/num2))
else:
    print("invalid choise")


