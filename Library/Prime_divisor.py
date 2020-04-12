def gcd(a, b):
    """a,bの最大公約数"""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def gcdlist(l):
    """リスト l の最大公約数"""
    a = l[0]
    for i in range(len(l)):
        a = gcd(a, l[i])
    return a


def extgcd(a, b):
    """互いに素なa,bについて、a*x+b*y=1の一つの解"""
    r = [1, 0, a]
    w = [0, 1, b]
    while w[2] != 1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0], r[1]-q*w[1], r[2]-q*w[2]]
        r = r2
        w = w2
    # [x,y]
    return [w[0], w[1]]


def extgcd_2(a, b):
    """a*x+b*y=gcd(a,b)の一つの解"""

    g = gcd(a, b)
    a = a//g
    b = b//g
    return extgcd(a, b)


def lcm(a, b):
    """a,bの最小公倍数"""
    return a * b // gcd(a, b)


def is_prime(n):
    """ nの素数判定 """
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def divisor(n):
    """ nの約数列挙 """
    ass = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            ass.append(i)
            if i**2 == n:
                continue
            ass.append(n//i)
    return ass  # sortされていない


def prime_factor(n):
    """ nの素因数分解(O(n**0.5) """
    ass = []
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            ass.append(i)
            n = n//i
    if n != 1:
        ass.append(n)
    return ass


def fctr1(n):
    """ [[素因数,数]]を出力 """
    f = []
    c = 0
    r = int(n**0.5)
    for i in range(2, r+2):
        while n % i == 0:
            c += 1
            n = n//i
        if c != 0:
            f.append([i, c])
            c = 0
    if n != 1:
        f.append([n, 1])
    return f


def primes(n):
    """ n以下の素数列挙(O(n log(n)) """
    ass = []
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    for i in range(len(is_prime)):
        if is_prime[i]:
            ass.append(i)
    return ass


def segment_sieve(a, b):
    """ a以上b未満の素数列挙 """
    ass = []
    is_prime_small = [True] * (int(b**0.5)+1)
    is_prime = [True] * (b-a)
    for i in range(2, int(b**0.5)):
        if is_prime_small[i]:
            j = 2*i
            while j**2 < b:
                is_prime_small[j] = False
                j += i
            j = max(2*i, ((a+i-1)//i)*i)
            while j < b:
                is_prime[j-a] = False
                j += i
    for i in range(len(is_prime)):
        if is_prime[i]:
            ass.append(a+i)
    if ass[0] == 1:
        del ass[0]
    return ass


#####################
print(is_prime(53))
print(sorted(divisor(20)))  # sortしてる
print(prime_factor(18))
print(fctr1(60))
print(primes(100))
print((segment_sieve(1, 101)))

# 12,18の最大公約数
print(gcd(12, 18))

# [6,9,15,213]の最大公約数
print(gcdlist([6, 9, 15, 213]))

# 5x + 17y = 1の解
print(extgcd(5, 17))

# 15x + 9y = gcd(15,9) = 3の解
print(extgcd_2(15, 9))

# 3,4の最小公倍数
print(lcm(3, 4))
