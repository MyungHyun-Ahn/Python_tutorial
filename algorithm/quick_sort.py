def swap_elements(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

def partition(my_list, start, end):
    i = start
    b = start
    p = end
    while i < p:
        if my_list[i] <= my_list[p]:
            swap_elements(my_list, i, b)
            b+=1
        i+=1
    swap_elements(my_list, b, p)
    return b

def quicksort(my_list, start, end):
    if end-start < 1:
        return
    pivot = partition(my_list, start, end)
    quicksort(my_list, start, pivot-1)
    quicksort(my_list, pivot+1, end)
# 옵셔널 파라미터 설정
def quicksort(my_list, start=0, end=None):
    if end == None:
        end = len(my_list) - 1
    if end-start < 1:
        return
    pivot = partition(my_list, start, end)
    quicksort(my_list, start, pivot-1)
    quicksort(my_list, pivot+1, end)

# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1, 0, len(list1) - 1)
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2, 0, len(list2) - 1)
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3, 0, len(list3) - 1)
print(list3)