n = int(input())
a = list(map(int, input().split()))
odds = 0
evens = 0
for i in a:
    if i % 2 == 0:
        evens += 1
    else:
        odds += 1
if evens and odds:
    print(*sorted(a))
else:
    print(*a)
    