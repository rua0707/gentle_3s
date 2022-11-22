# def solution(numbers):
#     answer = []

#     for num in numbers:
#         if num % 2 == 0:
#             answer.append(num+1)
#             continue
        
#         num_bin = "0" + bin(num)[2:]
#         num_bin = num_bin[:num_bin.rindex("0")] + "10" + num_bin[num_bin.rindex("0") + 2:]
#         answer.append(int(num_bin, 2))

#     return answer

a = "0" + bin(17)[2:]
print(a + "   >>")
print(a[:a.rindex("0")] + "10")
a = a[:a.rindex("0")] + "10" + a[a.rindex("0") + 2:]
print(a)
print(int(a, 2))