def my_binary_search(element, some_list):
    max_val = len(some_list)
    min_val = 0
    
    while True:
        medium_val = int((max_val + min_val) / 2)
        if some_list[min_val] > element:
            return None
        if some_list[max_val-1] < element:
            return None
        medium_val = int((max_val+min_val) / 2)
        
        if some_list[medium_val] == element:
            return medium_val
        elif some_list[medium_val] > element:
            max_val = medium_val
        elif some_list[medium_val] < element:
            min_val = medium_val
        else:
            return None 
    return None

def codeit_binary_search(element, some_list):
    min_index = 0
    max_index = len(some_list) - 1

    while min_index <= max_index:
        medium_index = (min_index + max_index) // 2
        if some_list[medium_index] == element:
            return medium_index
        elif some_list[medium_index] > element:
            max_index = medium_index - 1
        else:
            min_index = medium_index + 1
    return None

def main():
    print(my_binary_search(2, [2, 3, 5, 7, 11]))
    print(my_binary_search(0, [2, 3, 5, 7, 11]))
    print(my_binary_search(5, [2, 3, 5, 7, 11]))
    print(my_binary_search(3, [2, 3, 5, 7, 11]))
    print(my_binary_search(11, [2, 3, 5, 7, 11]))
    print('-------------------------------------')
    print(codeit_binary_search(2, [2, 3, 5, 7, 11]))
    print(codeit_binary_search(0, [2, 3, 5, 7, 11]))
    print(codeit_binary_search(5, [2, 3, 5, 7, 11]))
    print(codeit_binary_search(3, [2, 3, 5, 7, 11]))
    print(codeit_binary_search(11, [2, 3, 5, 7, 11]))

if __name__ == '__main__':
    main()