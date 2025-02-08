def spy_game(nums):
    n = 0  
    for num in nums:
        if num == 0 and n == 0:  
            n = 1
        elif num == 0 and n == 1:  
            n = 2
        elif num == 7 and n == 2:  
            return True  
    return False  

print(spy_game([1, 2, 4, 0, 0, 7, 5]))  
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  
