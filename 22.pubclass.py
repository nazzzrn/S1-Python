class publisher:
    def __init__(self,nm):
        self._name=nm
    def display(self):
        print("The publisher name is:",self._name)
class book(publisher):
    def __init__(self,nm,ttl,auth):
        super().__init__(nm)
        self._title=ttl
        self._author=auth
    def display(self):
        super().display()
        print("The title of the book is:",self._title)
        print("The author of the book is:",self._author)
class python(book):
    def __init__(self,nm,ttl,auth,prc,nopg):
        super().__init__(nm,ttl,auth)
        self._price=prc
        self._npages=nopg
    def display(self):
        super().display()
        print("The book price is:",self._price)
        print("No of pages is:",self._npages)
n=input("Enter the publisher name:")
t=input("Enter the title of the book:")
a=input("Enter the author name:")
p=input("Enter the price of the book:")
pg=input("Enter the number of pages in the book:")

p1=python(n,t,a,p,pg)
print("The entered book details are:")
p1.display()



