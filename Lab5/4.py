import re

def find_sequence(blabla):
    pattern=r"\b[A-Z][a-z]+\b"
    match=re.findall(pattern, blabla )
    return match 


print(find_sequence("GHHHHek knwnwkfnwlo Hhfowjow"))