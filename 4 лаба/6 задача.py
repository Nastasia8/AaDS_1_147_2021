
def fun(sp):
    a=list()
    [a.append(num) for num in sp if num not in a]
    return tuple(a)
numbers=[int(num) for num in input().split()]
fun(numbers)

print(fun(numbers))