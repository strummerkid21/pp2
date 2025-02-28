import re
def snakecamel(snake_str):
    words=snake_str.split("_")
    return words[0]+" ".join(word.capitalize() for word in words[1:])

print(snakecamel("snake_str"))