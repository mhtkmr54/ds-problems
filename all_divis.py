from collections import defaultdict


def primes_power(n):
    primfac = defaultdict(int)
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac[d] += 1  # counter for the power of the prime
            n //= d
        d += 1
    if n > 1:
        primfac[n] += 1
    print primfac
    powers = list(primfac.values())
    print powers
    total_divisors = 1
    for a in  powers:     #getting total no. of divisors
        total_divisors *= (a+1) 
    print total_divisors
    return total_divisors - 1 

print primes_power(50)
