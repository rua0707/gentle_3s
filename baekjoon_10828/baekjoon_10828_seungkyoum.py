import sys

n = int(sys.stdin.readline())

stack_ = []
for _ in range(n):
    order = sys.stdin.readline().split()

    if order[0] == "push":
        stack_.append(int(order[1]))
    elif order[0] == "pop":
        if len(stack_) == 0:
            print(-1)
        else:
            print(stack_.pop())
    elif order[0] == "size":
        print(len(stack_))
    elif order[0] == "empty":
        if len(stack_) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == "top":
        if len(stack_) == 0:
            print(-1)
        else:
            print(stack_[-1])