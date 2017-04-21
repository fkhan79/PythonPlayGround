def primes(n):
    factorials = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            factorials.append(d)
            n //= d
        d += 1
    if n > 1:
       factorials.append(n)
    print(factorials)
    return factorials

primes(600851475143)