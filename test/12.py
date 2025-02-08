def histogram(l):
    for num in l:
        print('*' * num)  


numbers = input("").split()
numbers = [int(i) for i in numbers] 
histogram(numbers)
