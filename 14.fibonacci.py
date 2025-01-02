while(1):
    n=int(input("Enter the limit:\n"))
    x=0
    y=1
    if n>1:
        print(x,end=" , ")
    if n>2:
        print(y,end=" , ")
    for i in range (2,n):
        s=x+y
        print(s,end=" , ")
        x=y
        y=s
    print("\n")