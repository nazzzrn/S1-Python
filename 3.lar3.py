a=int(input("Enter the first number:\n"))
b=int(input("Enter the second number:\n"))
c=int(input("Enter the third number:\n"))
if a>b and a>c:
    print(a,"is largest")
elif b>a and b>c:
    print(b,"is largest")
else:
    print(c,"is largest")