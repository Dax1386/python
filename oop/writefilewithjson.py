import json
student = {
            "dax": 8.69, 
            "heet": 8.65, 
            "ishan": 8.00,
            "smit": 8.55,
            "ansh": 7.93
            }

file_path = "oop/new.txt"
try:
    with open(file_path , "w") as file:
        json.dump(student,file , indent=4)
        print(f"student list insert in {file_path}")
except FileExistsError:
    print("file is already exist")