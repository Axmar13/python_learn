def dig_pow(n, p):
    result = result_2 = k = 0
    result = sum([int(num) ** (p + i) for i, num in enumerate(str(n))])
    return result//n if result%n==0 else -1

print(dig_pow(46288, 3))