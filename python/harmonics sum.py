#harmonic series

def harmonics(n):
    if n==1:
        return n
    else:
        return (1/n)+((harmonics(n-1))/1)

a=int(input(""))
print(harmonics(a))