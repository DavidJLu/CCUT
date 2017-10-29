n = 0
m = 1
for i in range(1, 1000000):
    temp = n + m
    n = m
    m = temp
print(n)
input()