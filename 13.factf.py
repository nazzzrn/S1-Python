while(1):
    a=int(input("Enter the limit:\n"))
    def fact(b):
        if(b):
            f=b*fact(b-1)
            return f
        else:
            return 1
    print("The factorial is",fact(a))