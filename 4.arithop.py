while(1):
    a=int(input("Enter the first number:\n"))
    b=int(input("Enter the second number:\n"))

    c=int(input("Choose the operation:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Reminder\n"))
    if(c==1):
        print("The sum is ",a+b)
    elif(c==2):
        print("The difference is ",a-b)
    elif(c==3):
        print("The product is",a*b)
    elif(c==4):
        print("The quotient is",a/b)
    elif(c==5):
        print("The reminder is",a%b)
    else:
        print("no option is choosed")
        break