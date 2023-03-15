#recursion = function calling itself 
#we can set the limit of recursion


#factorial of a number using recursion 

a= int(input(""))
sum=1

def fact(b):
    if b==1:
        return b
    else:
        return b*fact(b-1)

print(fact(a))

