"""

#object= name, name1
#class= mysamples

class mysamples:
    def athul(value,a):
        value.name=a
    def printname(value):
        print(value.name)


name=mysamples()
name1=mysamples()
name2=mysamples()

a="hai"
b="athul"
c="gn"

name.athul(a)
name1.athul(b)
name2.athul(c)

name.printname()
name1.printname()
name2.printname()
"""

class students:
    def namefunction(a,b):
        print("name is ",b)
    def agefunction(a,b):
        print("age is ",b)

name=students()
age=students()

name1=input(" enter your name : ")
age1=int(input("enter your age : "))

name.namefunction(name1)
age.agefunction(age1)

