# def odd_even(my_list):
#     odd_list = [odd for odd in my_list if odd%2 == 1]
#     even_list = [even for even in my_list if even%2 == 0]
#     print(odd_list+even_list)


def odd_even(my_list):
    front_pointer = 0
    tail_pointer = len(my_list) - 1

    while front_pointer < tail_pointer:
        if my_list[front_pointer]%2 == 1:
            if my_list[tail_pointer]%2 == 0:
                tmp = my_list[front_pointer] 
                my_list[front_pointer] = my_list[tail_pointer]
                my_list[tail_pointer] = tmp
            else:
                tail_pointer -= 1
        else:
            front_pointer += 1
    
    print(my_list)

odd_even([3])