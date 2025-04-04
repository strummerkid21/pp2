import os

#task 1
def list_content(path):
    all_items = os.listdir(path)

    print(os.path.isdir(os.path.join(path)))

    directories = [item for item in all_items if os.path.isdir(os.path.join(path, item))]
    files = [item for item in all_items if os.path.isfile(os.path.join(path, item))]

    print("all items: ", all_items)
    print("directories: ", directories)
    print("files: ", files)

path = "."
list_content(path)

#task 2
print('Exist:', os.access(path, os.F_OK))
print('Readable:', os.access(path, os.R_OK))
print('Writable:', os.access(path, os.W_OK))
print('Executable:', os.access(path, os.X_OK))

#task 3
path = input("=")
if os.path.exists(path):
    print(os.path.dirname(path))
    print(os.path.basename(path))
else:
    print("path does not exist")

#task 4
cnt = 0
with open('dir-and-files.txt', 'r', encoding='utf-8') as f:
    for _ in f:
        cnt+=1

print(cnt)

#task 5
lst = [1,2,3,4,5,6,7,8]
with open('newfile.txt', 'w') as f:
    for i in lst:
        f.write(str(i) + '\n')

#task 6

for i in range(65, 91):
    with open(f'{chr(i)}.txt', 'w') as f:
        f.write(" ")

#task 7
with open('dir-and-files.txt', 'r') as rd, open('newfile.txt', 'w') as wt:
    wt.write(rd.read())


#task 8
df = 'A.txt'
if os.path.exists(df):
    if os.access(df, os.F_OK):
        os.remove(df)
    else:
        print("Permision denied")
else:
    print("does not exist")