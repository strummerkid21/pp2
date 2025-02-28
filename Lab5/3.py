import re

def find_sequence(blabla):
    pattern=r"\b[a-z]+_[a-z]+\b"
    match=re.findall(pattern, blabla)
    return match is not None
    
print(find_sequence("jfwijof_feknf"))