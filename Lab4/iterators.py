mytuple=("cherry", "banana", "apples")
myiter=iter(mytuple)
print(next(myiter))
print(next(myiter))
print(next(myiter))


mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


mytuplee=("banana", "cherry")
for x in mytuplee:
    print(x)
    
    
mystr="hello"
for x in mystr:
    print(x)
    

class mynumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
myclass=mynumbers()
myiter=iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))