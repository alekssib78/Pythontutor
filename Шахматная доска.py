a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a % 2 == c % 2:
    if b % 2 == d % 2:
        print('YES')
    else:
        print('NO')
else:
    if b % 2 != d % 2:
        print('YES')
    else:
        print('NO')
