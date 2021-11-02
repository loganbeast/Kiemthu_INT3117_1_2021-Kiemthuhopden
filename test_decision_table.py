from main import check_fibonacci_sum_divide_nine
def test_case_1():
    assert check_fibonacci_sum_divide_nine(610, 56) == True
def test_case_2():
    assert check_fibonacci_sum_divide_nine(377, 56) == False
def test_case_3():
    assert check_fibonacci_sum_divide_nine(300, 56) == False
def test_case_4():
    assert check_fibonacci_sum_divide_nine(500, 101) == False
def test_case_5():
    assert check_fibonacci_sum_divide_nine(1001, 50) == False


