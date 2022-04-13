def merge(list1, list2):
    i=0
    j=0
    list3 = []
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            list3.append(list2[j])
            j+=1
        elif list1[i] <= list2[j]:
            list3.append(list1[i])
            i+=1
    if i == len(list1):
        list3 = list3 + list2[j:]
    if j == len(list2):
        list3 = list3 + list1[i:]
    return list3

def merge_sort(my_list):
    n = len(my_list)
    if n == 2:
        return merge(my_list[:1], my_list[1:])
    if n == 3:
        return merge(my_list[:1], my_list[1:])
    list1 = my_list[:n//2]
    list2 = my_list[n//2:]
    return merge(merge_sort(list1), merge_sort(list2))

print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
