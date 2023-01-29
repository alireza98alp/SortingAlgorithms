def QuickSort(list):
    if len(list)==2:
        return[min(list),max(list)]
    elif len(list)<2:
        return list
    else:
        pivot=list[0]
        l1=[]
        l2=[]
        for num in list[1:]:
            l1.append(num) if num<=pivot else l2.append(num)
    return QuickSort(l1)+[pivot]+QuickSort(l2)