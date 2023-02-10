def BubbleSort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1):
            if list[i]>list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
        print(list)
    return list
print(BubbleSort([5,9,6,2,15,3,18,9,7,18,10,20,11,26,14]))