import sys

N = int(sys.stdin.readline())



if N == 0:
    print(0)
elif N == 1:
    print(1)
elif N == 2:
    print(1)
else:
    arr = [0,1,1]

    for i in range(3,N+1):
        arr.append(arr[i-1]+arr[i-2])
    print(arr[-1])