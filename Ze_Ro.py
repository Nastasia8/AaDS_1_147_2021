elements = '14, 46, 10, -78, 0, 6, -31, -24, 56, 17, -83, -4'
result = ''
n = 0

while n < len(elements):
    if int(elements[n]) > 0:
        result += '+'
    elif int(elements[n]) < 0:
        result += '-'
    else:
        result += '0'
    n += 1
result = dict(zip(elements, result))
print(result)