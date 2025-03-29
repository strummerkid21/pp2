import math
import time

# multiply all the numbers in a lis
def multiply_list(nums):
    return math.prod(nums)  

nums = [2, 3, 4, 5]
print(multiply_list(nums))  



# number of upper case letters and lower case letters
def count_case(text):
    upper = sum(1 for char in text if char.isupper())
    lower = sum(1 for char in text if char.islower())
    return upper, lower

text = "Hello World!"
upper_count, lower_count = count_case(text)
print("Upper:", upper_count, "Lower:", lower_count)  



# palindrome
def is_palindrome(word):
    return word == word[::-1]

word = "radar"
print(is_palindrome(word))  



# square root function after specific milliseconds
def delayed_sqrt(num, delay_ms):
    time.sleep(delay_ms / 1000)  
    return math.sqrt(num)

num = int(input())
delay_ms = int(input())
print(f"Square root of {num} after {delay_ms} milliseconds is {delayed_sqrt(num, delay_ms)}")




# True if all elements of the tuple are true
def all_true(values):
    return all(values)

values_input = input("").split()

values = []
for x in values_input:
    if x.isdigit(): 
        values.append(int(x) != 0)
    else:
        values.append(False)  

values = tuple(values) 
print( all_true(values))
