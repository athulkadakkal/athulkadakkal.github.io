#lambda=function without name.

#f=lambda a: a*a
#print(f(7))

#result = lambda a,b:a+b
#print(result(1,2))

"""
 question 1 : wap to add 15 to given number .also create  a lambda fn that multiplies  argumnet x with y  , then print result

x= int(input(""))
y=int(input(""))

add= lambda x:x+15
sum = lambda x,y: x*y

print(add(x),sum(x,y))

"""


""" qn 2: write a program to create a function  that take  an argument will be multiplied by an unknown givn number """
'''
x=int(input(""))
val=15
result= lambda a: val* a

print(result(x))
'''


''' qn 3 : wap to  list the integers using lambda (even,odd)

a= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

even=list(filter(lambda a: a%2==0 ,a))
odd= list (filter(lambda a: a%2!=0,a))

print(even,"\n",odd)'''



'''qn 4: wap to squre and cube every number in the list 
a=[1,2,3,4,5,6,7,8,9]
s=list(map(lambda a: a*a,a))
c=list(map(lambda a: a*a*a,a))

print(s,"\n",c)'''

'''qn 5 : write a python program to find  if a given string starts with given character

string=input("")
character=input("")
result= lambda : string[0]==character
print(result())

'''






































