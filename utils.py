def factor(n):
    if n < 0:
        return 
        
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factor(5)) 

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

