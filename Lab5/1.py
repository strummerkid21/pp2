import re

def match_string(input_string):
    pattern=r"^a*b*$"
    match=re.fullmatch(pattern, input_string)
    return match is not None

print(match_string("abbbb"))