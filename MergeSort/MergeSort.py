def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    
    while i < len(list1):
        combined.append(list1[i])
        i += 1

    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined

def merge_sort(mylist):
    if len(mylist) == 1:
        return mylist
    middle = len(mylist)//2
    front = mylist[:middle]
    tail = mylist[middle:]
    return merge(merge_sort(front), merge_sort(tail))


print(merge_sort([5,3,6,1,3,2,4]))
    
