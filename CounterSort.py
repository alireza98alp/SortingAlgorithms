def CounterSort(list):
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
        list+=[minimum]*counter[k]
        minimum+=1
    return list
