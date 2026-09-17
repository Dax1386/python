import csv

list = [["name","age","cgpa"],["dax",20,8.69],["heet",19,8.65],["ishan",19,8.00]]

file_path = "oop/new.txt"
try:
    with open(file_path , "w" , newline="") as file:
        writer = csv.writer(file)
        for row in list:
            writer.writerow(row)
            print(f"list insert in {file_path}")
except FileExistsError:
    print("file is already exist")