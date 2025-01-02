print("program to find greatest common divisor of two numbers")
while(1):
    a=int(input("Enter the first number:\n"))
    b=int(input("Enter the second number:\n"))
    for i in range(min(a,b),0,-1):
        if(a%i==0 and b%i==0):
            print(f"{i} is the gcd of {a} and {b}")
            break