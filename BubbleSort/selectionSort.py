def selectionSort(my_list):
    for i in range(len(my_list) -1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[min_index]
            my_list[min_index] = my_list[i]
            my_list[i] = temp

    return my_list


print(selectionSort([3,6,1,7,2,8]))



