
def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index

def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index-1)
        quick_sort_helper(my_list, pivot_index+1, right)
    return my_list

def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list)-1)

def main():
    ### Test swap function
    swaplist = [4, 6, 2, 8, 1]
    swap(swaplist, 0, 3)
    print(type(swaplist))
    print(swaplist)

    ### Test pivot function
    plist = [5, 4, 6, 1, 3, 2]
    print("list is [{}]".format(plist))
    print("Pivot indexes 0 and 5")
    print(pivot(plist, 0, 5))
    print(plist)

    ### Test quicksort
    print(quick_sort([4,6,1,7,3,2,5]))

if __name__ == "__main__":
    main()
