#filter( functon, iteration )= filter the numbers from list



nums=[1,2,3,4,5,6,7,8,9]

evens=list(filter(lambda a:a%2!=0,nums))

print(evens)