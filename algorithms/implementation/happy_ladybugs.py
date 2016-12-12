from collections import Counter


def solve(b):
    counter = Counter(b)
    if any([counter[k] < 2 for k in counter if k != '_']):
        return 'NO'
    if '_' in counter or (all([b[i - 1] == b[i] or b[i + 1] == b[i] for i in range(1, len(b) - 1)]) and b[0] == b[1] and b[-1] == b[-2]):
        return 'YES'
    return 'NO'

for _ in range(int(input())):
    input()
    b = input()
    print(solve(b))
