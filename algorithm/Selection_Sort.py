def selection_sort(sort_list):
    for i in range(len(sort_list)-1):
        min_index = i
        for j in range(i, len(sort_list)):
            if sort_list[j] < sort_list[min_index]:
                min_index = j
        sort_list[i], sort_list[min_index] = sort_list[min_index], sort_list[i]

    return sort_list

def main():
    print(selection_sort([4, 5, 2, 1, 4, 6, 7]))


if __name__ == '__main__':
    main()
        

            