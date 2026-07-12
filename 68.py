def add(a, b):
    return a + b


def test_add():
    a = 10
    b = 20

    result = add(a, b)

    assert result == 30

    print("test passed")

test_add()