minutes = [0, 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'ninteen', 'twenty']
quarters = ["%s o' clock", "quarter past %s", "half past %s", "quarter to %s"]
for i in range(1, 10):
    minutes.append('twenty %s' % minutes[i])

h, m = int(input()), int(input())
hour = minutes[h + (m > 30)]
if not m % 15:
    print(quarters[m // 15] % hour)
elif m < 30:
    print("%s minute" % minutes[m] + "s" * (m != 1) + " past %s" % hour)
else:
    print("%s minute" % minutes[60 - m] + "s" * (m != 59) + " to %s" % hour)
