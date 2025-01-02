class time:
    def __init__(self,h,m,s):
        self.hour=h
        self.minute=m
        self.second=s
    def __add__(self,other):
        h=self.hour+other.hour
        m=self.minute+other.minute
        s=self.second+other.second
        while s>=60:
            s=s-60
            m=m+1
        while m>=60:
            m=m-60
            h=h+1
        if h>24:
            h=h%24
        return h,m,s
    def display(self):
        print(self.hour,":",self.minute,":",self.second)
print("Enter the first time:")
h1=int(input("Hours:"))
m1=int(input("Minutes:"))
s1=int(input("Seconds:"))
t1=time(h1,m1,s1)

print("Enter the second time:")
h2=int(input("Hours:"))
m2=int(input("Minutes:"))
s2=int(input("Seconds:"))
t2=time(h2,m2,s2)

t3=list(t1+t2)

print("The sum of the time is",t3[0],":",t3[1],":",t3[2])


        