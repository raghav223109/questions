from multiprocessing import Process

def task():
    print("downloading")


if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    p.join()