a = [3, 8, 2, 1, 4, 7, 5, 6, 10, 9]
def calc(a):
    return a % 2 == 0
filtred = list(filter(calc,a))
print(filtred) 