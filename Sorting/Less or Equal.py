n, p = map(int, input().split())
a = list(map(int, input().split()))

lef = 1
rig = 10**9

while lef <= rig:
    midle = (lef + rig) // 2
    c = 0
    for i in range(n):
        if a[i] <= midle:
            c += 1
    if c == p:
        print(midle)
        break
    elif c < p:
        lef = midle + 1
    else:
        rig = midle - 1

if lef > rig:
    print(-1)

	  				   						 						       	