# # 분해합
# N = int(input)
# res = 0

# for i in range(1, N+1):
#     N_list = list(map(int, str(i)))
#     res = i + sum(N_list)
#     if res == N:
#         print(i)
#         break

#     if i == N:
#         print(0)



N = int(input())
result = 0

for i in range(1, N+1):        
    a = list(map(int, str(i)))  
    s = i + sum(a)              
    if(s == N):                 
        result = i                   
        break

print(result)