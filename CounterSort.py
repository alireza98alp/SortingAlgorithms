def CounterSort(list):
    lenght=len(list)
    maximum=max(list)
    minimum=min(list)
    counter=[0]*(maximum-minimum+1)
    number=minimum
    for i in range(maximum-minimum+1):
        for n in list:
            if n==number:
                counter[i]+=1
        number+=1
    list=[]
    for k in range(len(counter)):
        list += [minimum] * counter[k]
        minimum+=1    
    return list
# list=[-2,5,4,1,5,6,3,3,3,3,3,3,2,1,0,0,0,2,2,2,2,12,0,3]
# print(CounterSort(list))