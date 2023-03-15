#wap  to calc  the sum of list of numbers

def list_sum(num_list):

    if len(num_list)==1:
        return num_list[0]
    else:
        return num_list[0]+list_sum(num_list[1:])
    
aa=[1,2,[3,4]]
print(list_sum(aa))