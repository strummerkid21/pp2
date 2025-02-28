import re

txt="The rain in  Spain"
x=re.search("\s", txt)
y = re.split("\s", txt)

print(y)

print("position of first white space:", x.start())


import re

txt = "The rain in Spain"
x = re.split("\s", txt, 2)
y=re.sub("\s", "9", txt)

print(x,y)

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())


import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)


import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())


