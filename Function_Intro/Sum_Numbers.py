def sum_numbers(*args: float) -> float:
    """Return sum of values"""
    total = 0
    for i in args:
        total += i
    return total


print(sum_numbers(1, 2, 3))

# ctrl + shift + R 切换至当前页运行代码
# ctrl + R 运行指向页面（即刚运行过的页面）
