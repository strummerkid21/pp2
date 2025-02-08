def unique_elements(lst):
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    return new_list

numbers = input("").split()
numbers = [int(i) for i in numbers] 
print(unique_elements(numbers))