print('x^')
x = float(input())
print('y^')
y = float(input())
stepen = list(range(1, 21))
i = 0

while i < len(ps):
    if stepen[i] % 2 != 0:
        stepen[i] = stepen[i]**x**y
    i += 1

print(*stepen)
