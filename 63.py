import threading
import threading

def task():
    print("downloading")

t = threading.Thread(target=task)

t.start()
t.join()