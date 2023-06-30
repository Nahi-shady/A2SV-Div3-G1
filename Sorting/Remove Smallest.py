t = int(input())

for _ in range(t):
     n = int(input())
     a = list(map(int, input().split()))
     
     a.sort()
     state = True
     for i in range(n-1):
          if a[i+1] - a[i] > 1:
              state = False
              break
     if state:
          print('yes')
     else:
          print('no')
          
