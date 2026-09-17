employees = ["dax" , "heet" , "ishan" , "smit" ,"ansh"]

file_path = "oop/output.txt"
try:
    with open(file_path , "w") as file:
        for employee in employees:
            file.write(employee + " ")
            print(f"emloyee list insert in {file_path}")
except FileExistsError:
    print("file is already exist")