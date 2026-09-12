# Args and Kwargs in Python

def my_function(*args, **kwargs):

    for arg in args:
        print(arg , end = " ")
        print()

    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
my_function("Varsadiya" , "Dax" , "B.tech",  "information technology",
                      name = "Varsadiya Dax", age = 20, branch = "Information Technology")