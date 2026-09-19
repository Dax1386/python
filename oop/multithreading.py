import threading
import time

def play():
    time.sleep(5)
    print("playing cricket")

def study():
    time.sleep(3)
    print("learn python")
    
def college():
    time.sleep(2)
    print("went to the college")

go1 = threading.Thread(target=play)
go1.start()
go2 = threading.Thread(target=study)
go2.start()
go3 = threading.Thread(target=college)
go3.start()

go1.join()
go1.join()
go1.join()

print("all task complete")

