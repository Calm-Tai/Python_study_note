import threading
import time


def print_times(name, _time):
    i = 1
    while i <= 5:
        time.sleep(_time)
        print(name, i)
        i += 1


th1 = threading.Thread(target=print_times, args=("aaa2", 3))
th2 = threading.Thread(target=print_times, args=("aaa1", 5))

th1.start()
th2.start()
