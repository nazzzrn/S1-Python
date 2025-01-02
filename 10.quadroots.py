import math
while(1):    
    print("A quadratic equation is of the form: ax^2+bx+c")
    a=int(input("Enter the value of a:"))
    b=int(input("Enter the value of b:"))
    c=int(input("Enter the value of c:"))
    d=b*b-4*a*c
    if(d>0):
        print(f"The quadratic equation has two real and distinct roots{-b+math.sqrt(d)/(2*a)} and {-b-math.sqrt(d)/(2*a)}")
    if(d==0):
        print(f"The quadratic equation has real equal root {-b/(2*a)}")
    if(d<0):
        print(f"The quadratic equation has two imaginary and distinct roots{-b/(2*a)} + {math.sqrt(abs(d))/(2*a)}i and {-b/(2*a)} - {math.sqrt(abs(d))/(2*a)}i")