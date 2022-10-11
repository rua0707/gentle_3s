import sys

card_list = [i for i in range(21)]

for _ in range(10):
    start_num, end_num = map(int, sys.stdin.readline().split())
    if (end_num - start_num) % 2 != 0:  # 구간의 차이가 홀수이면, 짝수갯수를 바꿈 ex) 5~10 = 5,6,7,8,9,10
        while start_num <= end_num:
            card_list[start_num], card_list[end_num] = card_list[end_num], card_list[start_num]
            start_num += 1
            end_num -= 1
    else:
        while start_num != end_num:
            card_list[start_num], card_list[end_num] = card_list[end_num], card_list[start_num]
            start_num += 1
            end_num -= 1

for i in card_list[1:]:
    print(i, end=" ")


######################## 다른사람 코드 #########################
arr = [i for i in range(0, 21)]

for _ in range(10):
    a, b = map(int, input().split())
    b += 1
    arr_ = arr[:a] + arr[a: b][::-1] + arr[b:]
    arr = arr_

print(' '.join(map(str, arr[1:])))
