N = int(input())
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_prime_product_pair(N):
    for i in range(2, N):
        if is_prime(i) and N % i == 0:
            quotient = N // i
            if is_prime(quotient) and i != quotient:
                return i, quotient
    return -1
result = find_prime_product_pair(N)
if result != -1:
    print(result[0], result[1])
else:
    print(-1)
