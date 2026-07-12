def numbers():
    for i in range(5):
        yield i

for x in numbers():
    print(x)