# Enter your code here. Read input from STDIN. Print output to STDOUT
lim = 100

def primes_sieve(limit):
    limitn = limit+1
    not_prime = [False] * limitn
    primes = []

    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in xrange(i*2, limitn, i):
            not_prime[f] = True

        primes.append(i)

    return primes

a = primes_sieve(lim)
p = []
p.append(1)

for i in a:
    if lim%i == 0:
        p.append(i)
         
print a
print p

k = {}
for el in p:
    k[el] = lim/el
print k


-----------------------------------------



def divisors(n):
    # get factors and their counts
    factors = {}
    nn = n
    i = 2
    while i*i <= nn:
        while nn % i == 0:
            if not i in factors:
                factors[i] = 0
            factors[i] += 1
            nn //= i
        i += 1
    if nn > 1:
        factors[nn] = 1

    primes = list(factors.keys())

    # generates factors from primes[k:] subset
    def generate(k):
        if k == len(primes):
            yield 1
        else:
            rest = generate(k+1)
            prime = primes[k]
            for factor in rest:
                prime_to_i = 1
                # prime_to_i iterates prime**i values, i being all possible exponents
                for _ in range(factors[prime] + 1):
                    yield factor * prime_to_i
                    prime_to_i *= prime

    # in python3, `yield from generate(0)` would also work
    for factor in generate(0):
        yield factor
        
        
        
#---------------------------------final --------------------------------------------------------
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict


boolean isWinning(position pos) {
    moves[] = possible positions to which I can move from the
position pos;
    for (all x in moves) 
        if (!isWinning(x)) return true;
    
    return false; 
}





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
    powers = list(primfac.values())
    print powers
    total_divisors = 1
    for a in  powers:     #getting total no. of divisors
        total_divisors *= (a+1) 
    print total_divisors
    return total_divisors

def main():
    T = int(input())
    for i in xrange(T):
        N = map(int, raw_input().strip().split())
        print N
        heights = map(int, raw_input().strip().split())
        print heights
        possible_heights = []
        for h in heights:
            possible.append()
            

        
if __name__ == '__main__':
    main()    








