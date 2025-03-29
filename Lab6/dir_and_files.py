import os
import shutil

#1 List directories, files, and both
def list_items(path):
    if not os.path.exists(path):
        print("Path does not exist!")
        return

    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    print("Directories:", dirs)
    print("Files:", files)
    print("All:", dirs + files)



#2 Check file or directory access
def check_access(path):
    print("Exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))



#3 Get file name and directory if path exists
def path_info(path):
    if os.path.exists(path):
        print("File name:", os.path.basename(path))
        print("Directory:", os.path.dirname(path))
    else:
        print("Path does not exist")



#4 Count lines in a file
def count_lines(file):
    if not os.path.exists(file):
        print("File not found!")
        return

    with open(file, "r", encoding="utf-8") as f:
        print("Line count:", len(f.readlines()))



#5 Write a list to a file
def write_list(file, data):
    with open(file, "w", encoding="utf-8") as f:
        f.writelines("\n".join(data))
    print(f"List written to {file}")



#6 Create 26 files (A.txt - Z.txt)
def create_files():
    for i in range(65, 91):  # ASCII A-Z
        with open(f"{chr(i)}.txt", "w") as f:
            f.write(f"File {chr(i)}")



#7 Copy file contents
def copy_file(src, dest):
    if not os.path.exists(src):
        print("Source file not found!")
        return

    shutil.copy(src, dest)
    print(f"Copied {src} to {dest}")

    

#8 Delete file if it exists and is writable
def delete_file(file):
    if os.path.exists(file):
        if os.access(file, os.W_OK):
            os.remove(file)
            print(f"File {file} deleted")
        else:
            print("No permission to delete file!")
    else:
        print("File not found!")





# 
path = input("Enter directory path: ")
list_items(path)

file = input("Enter file path: ")
check_access(file)
path_info(file)

count_lines(file)

data = ["line 1", "line 2", "line 3"]
write_list("output.txt", data)

create_files()

src = input("Enter source file path: ")
dest = input("Enter destination file path: ")
copy_file(src, dest)

file_to_delete = input("Enter file path to delete: ")
delete_file(file_to_delete)