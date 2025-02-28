import re

def camelsnake(camelcase_string):
    return re.sub(r"(?<!^)(?=[A-Z])", "_", camelcase_string)

print(camelsnake("HelloWorld"))