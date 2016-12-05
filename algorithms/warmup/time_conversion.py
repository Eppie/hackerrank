t = input()
h, m, a = t[:2], t[3:8], t[8]
if(h, a) == ('12', 'A'):
    h = '00'
if a == 'P' and '12' != h:
    h = str(int(h) + 12)
print(h + ':' + m)
