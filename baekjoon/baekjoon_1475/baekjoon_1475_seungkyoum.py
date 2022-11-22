import sys

ho = sys.stdin.readline().strip()
num_list = [0]*10

for i in range(len(ho)):
    num = int(ho[i])
    if num == 6 or num == 9:
        if num_list[6] <= num_list[9]:
            num_list[6] += 1
        else:
            num_list[9] += 1
    else:
        num_list[num] += 1
print(max(num_list))