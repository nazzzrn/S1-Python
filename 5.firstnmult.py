a=int(input("Enter the number for which the multiples are needed:\n"))
b=int(input("Enter the limit:\n"))
for i in range (1,b+1):
    print(f"{a}*{i}=",a*i)