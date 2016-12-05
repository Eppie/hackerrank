def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


n, friendly = map(int, input().split())
unfriendlies = set(map(int, input().split()))
unfriendlies = set([gcd(u, friendly) for u in unfriendlies])
divisors = set([friendly])
for i in range(2, int(friendly**0.5) + 1):
    if friendly % i == 0:
        divisors.add(i)
        divisors.add(friendly // i)
divisors -= unfriendlies
count = 0
for d in divisors:
    if any(u % d == 0 for u in unfriendlies):
        continue
    else:
        count += 1
print(count)
