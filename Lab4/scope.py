def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()



x = 300

def myfunc():
  print(x)

myfunc()

print(x)


def myfunc():
  global x
  x = 300

myfunc()

print(x)



def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())