n=int(input("Enter the number for which the factorial is needed:\n"))
result=1
for i in range(1,n+1):
    result=result*i
print(f"The factorial of {n} is {result}")