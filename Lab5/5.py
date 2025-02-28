import re

def find_string(input_string):
    pattern=r".*a.*b$"
    return re.match(pattern, input_string)

print(find_string("lmfelaammeomvb"))