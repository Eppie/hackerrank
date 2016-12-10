for _ in range(int(input())):
    b, w = map(int, input().split())
    x, y, z = map(int, input().split())
    a = y + z if min(x, z) == z and x != z and min(x, y + z) == y + z else x
    c = x + z if min(y, z) == z and y != z and min(x + z, y) == x + z else y
    result = b * a + w * c
    print(result)
