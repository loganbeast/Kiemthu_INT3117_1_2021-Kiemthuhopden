from main import check_fibonacci_sum_divide_nine
def test_case_miny_1():
    assert check_fibonacci_sum_divide_nine(610, -1) == False
def test_case_miny_2():
    assert check_fibonacci_sum_divide_nine(610, 0) == False
def test_case_miny_3():
    assert check_fibonacci_sum_divide_nine(610, 1) == False
def test_case_maxy_4():
    assert check_fibonacci_sum_divide_nine(610, 99) == False
def test_case_maxy_5():
    assert check_fibonacci_sum_divide_nine(610, 100) == False
def test_case_maxy_6():
    assert check_fibonacci_sum_divide_nine(610, 101) == True
def test_case_minx_7():
    assert check_fibonacci_sum_divide_nine(-1, 56) == False
def test_case_minx_8():
    assert check_fibonacci_sum_divide_nine(0, 56) == False
def test_case_minx_9():
    assert check_fibonacci_sum_divide_nine(1, 56) == False
def test_case_maxx_10():
    assert check_fibonacci_sum_divide_nine(999, 56) == False
def test_case_maxx_11():
    assert check_fibonacci_sum_divide_nine(1000, 56) == False
def test_case_maxx_12():
    assert check_fibonacci_sum_divide_nine(1001, 56) == False
def test_case_normal():
    assert check_fibonacci_sum_divide_nine(610, 56) == True