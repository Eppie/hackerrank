w, x, y, z = map(int, input().split())
a, b = y - w, z - x
print('YES' if a * b < 0 and a % b == 0 else 'NO')
