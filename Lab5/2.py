import re

def match_string(input_match):
    pattern=r"ab{2,3}"
    match=re.search(pattern, input_match)
    return match is not None
    
print(match_string("aaaaaabbsndfe"))
