def check_fibonacci_sum_divide_nine(x: int, y: int) -> int:
    fibonacci = []
    _next = None
    first = 0
    second = 1
    # loop to get all fibonacci
    for i in range(x + 1):
        if i <= 1:
            _next = i
        else:
            _next = first + second
            first = second
            second = _next
        fibonacci.append(_next)
    fibonacci = [f for f in fibonacci if f <= x]
    print(fibonacci)
    return True if x in fibonacci and (x + y) % 9 == 0 else False

print(check_fibonacci_sum_divide_nine(610,56))