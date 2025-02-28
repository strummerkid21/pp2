import re
def replace(blabla):
    pattern=r"[ ,.]"
    return re.sub(pattern, ":", blabla)

print(replace("Hello world, how.are?you"))