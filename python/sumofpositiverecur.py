#wap to calc the sum of +ve integers n+(n-2)+(n-4)+.........(n-x<=0)
#input=6    output=12
#input=10   output=30

def sumofpositive(n):
    if n<=0:
        return n
    else:
        return n+sumofpositive(n-2)
    
a=int(input(""))
print(sumofpositive(a))