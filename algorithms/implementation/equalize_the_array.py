from collections import Counter
input()
a = list(map(int, input().split()))
print(len(a) - Counter(a).most_common()[0][1])
