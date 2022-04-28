import threading
def print_hello_four_time():
    for i in range(4):
        print("Hello")

def print_susmita_four_time():
    for i in range(4):
        print("Susmita")

t1 = threading.Thread(target = print_hello_four_time)
t2 = threading.Thread(target = print_susmita_four_time)

t1.start()
t2.start()