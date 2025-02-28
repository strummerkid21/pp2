import re
txt="The rain in  Spain"
x=re.search("^The.*Spain$", txt)
y=re.findall("ai", txt)

print(x, y)





