import re

def splitt(blabla):
    return re.split(r"(?=[A-Z])", blabla)

print(splitt("HelloWorld"))