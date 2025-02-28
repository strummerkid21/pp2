import re

def addspace(sentence):
    return re.sub(r"(?<!^)(?=[A-Z])", " ", sentence)

print(addspace("HelloWorldHii"))