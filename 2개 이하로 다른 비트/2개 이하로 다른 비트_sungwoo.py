def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 == 0:
            bin_num = list(bin(num)[2:])
            bin_num[-1] = "1"
        else:
            bin_num = bin(num)[2:]
            bin_num = "0" + bin_num
            index = bin_num.rfind("0")
            bin_num[index] = "1"
            bin_num[index + 1] = "0"
        ans_num = int("".join(bin_num), 2)
        answer.append(ans_num)
    return answer호