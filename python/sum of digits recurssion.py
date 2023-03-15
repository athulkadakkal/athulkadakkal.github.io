#wap to print sum of digits of number

def sumofdigits(n):
    if n==0:
        return n
    else:
        return (n%10)+sumofdigits(int(n/10))
    
print(sumofdigits(int(input("enter number: "))))