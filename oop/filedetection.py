import os
file_name = "oop/test.txt"

if os.path.exists(file_name):
    print(f"the location of {file_name} exists")
else:
    print(f"{file_name} is not exists")
