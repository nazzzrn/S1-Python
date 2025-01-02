n=int(input("Enter the limit:\n"))
print(f"The first {n} even numbers are:100")
for i in range(0,2*n):
    if i%2==0:
        print(i)
s=(n/2)*(2*2+(n-1)*2)
print(f"The sum is {s}")
