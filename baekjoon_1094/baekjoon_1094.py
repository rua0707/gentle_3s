X = int(input())

bars = [32, 16, 8, 4, 2, 1, 1]

b_sum = []
for b in bars:
    if (b <= X) & ((sum(b_sum) + b) <= X):
        b_sum.append(b)

if X == 64:
    print(1)
else:
    print(len(b_sum))
