def print_permutations(word):
    def permute(s, answer):
        if len(s) == 0:
            print(answer)
            return
        
        for i in range(len(s)):
            ch = s[i]
            left = s[:i]
            right = s[i+1:]
            rest = left + right
            permute(rest, answer + ch)
    
    permute(word, "")

word = int(input(""))
print_permutations(word)