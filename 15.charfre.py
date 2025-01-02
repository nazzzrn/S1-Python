while(1):
    n=input("Enter the string:\n").lower()
    m=set(n.lower())
    for j in m:
        count=0
        for i in n:
            if i==j:
                count+=1
        print(f"The frequency of {j} in the string is {count}")

