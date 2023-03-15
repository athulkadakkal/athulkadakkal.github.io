size=int(input(""))

inp = input("")

aa=[]
bb=[]
sum=""

for x in range(len(inp)):
    if len(inp)-1==x:
        sum =  sum + inp[x]
        aa.append(int(sum))

    elif inp[x] != " " :
        sum =  sum + inp[x]
    
    else:
        aa.append(int(sum))
        sum=""
sum=""

for x in aa:
    sum=sum+str( x%10 )

if int(sum)%7==0:
    print("yes")
else:
    print("no")