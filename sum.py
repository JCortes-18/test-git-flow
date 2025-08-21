
def sum_numbers(a, b):
    return a + b

def test_sum_numbers():
    assert sum_numbers(1, 2) == 3
    assert sum_numbers(-1, 1) == 0
    assert sum_numbers(0, 0) == 0
    assert sum_numbers(100, 200) == 300

if __name__ == "__main__":
    test_sum_numbers()
    print("All tests passed!")
