#map( function, iterable)
#for reduce we import reduce from functools

from functools import reduce

a=[1,2,3,4,5,6,7,8,9,10]

double = list( map( lambda n:n*2 , a))
evens = list(filter(lambda n: n%2==0, a))
odd = list(filter(lambda n: n%2!=0,a))
sum= reduce(lambda c,b: c+b, a)

print(double,"\n",evens,"\n",odd,"\n", sum)