def insertion_sort(sort_list):
    for i in range(len(sort_list)-2):
        for j in range(0, len(sort_list)-1):
            if sort_list[j] > sort_list[j+1]:
                sort_list[j], sort_list[j+1] = sort_list[j+1], sort_list[j]

    return sort_list

def main():
    print(insertion_sort([4, 5, 2, 1, 4, 6, 7, 5, 3]))

if __name__ == '__main__':
    main()
   