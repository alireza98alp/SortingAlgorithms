def CounterSort(list):
    lenght=len(list)
    maximum=max(list)
    counter=[]
    for i in range(maximum):
        counter[i]=0
        for n in list:
            if i==n:
                counter+=1
    return counter
list=[5,4,12,0,3]
print(CounterSort(list))