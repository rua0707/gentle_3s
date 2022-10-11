import sys
n = int(sys.stdin.readline())

students = []
for _ in range(n):
    name, day, month, year = sys.stdin.readline().strip().split()
    day, month, year = map(int, (day, month, year))
    students.append((year, month, day, name))

students.sort()

print(students[-1][3])
print(students[0][3])