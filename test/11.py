def palindrome(text):
    return text == text[::-1]  

word = input("") 
print(palindrome(word)) 