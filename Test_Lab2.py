import Lab2Exercise6 as LAB2

def test_find_min_max():
    datalist = [1, 6, 4, 8, 3, 5]
    expected_result = (1, 8)
    test_result = LAB2.find_min_max(datalist)
    assert (test_result == expected_result)