"""You have been given 3 integers - l, r and k. Find how many numbers between l and r (both inclusive) are divisible by k. You do not need to print these numbers, you just have to find their count.

Input Format
The first and only line of input contains 3 space separated integers l, r and k.

Output Format
Print the required answer on a single line

input: 1 10 1
output: 10

"""

c1 = 0
sum=""
aa=[]
a=input("")
for x in a :
    if x!=" ":
        sum=sum+x
        c1+=1
        if c1==len(a):
            aa.append(int(sum))
    else:
        aa.append(int(sum))
        sum=""
        c1+=1
c1=0
l=aa[0]
r=aa[1]
k=aa[2]
for x in range (l,r+1) :
    if x%k==0:
        c1+=1
print(c1)
     