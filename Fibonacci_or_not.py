N = int(input())
def is_perfect_square(num):
    sqrt_num = int(num ** 0.5)
    return sqrt_num * sqrt_num == num
def is_fibonacci(num):
    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)
result = is_fibonacci(N)
print( result)
