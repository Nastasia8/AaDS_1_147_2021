def main():
    spisok = [1, 7, 4, 7, 15, 4, 7, 5, 2]
    print(funk(spisok))


def funk(numbers):
    for i in range(len(numbers)):
        k = numbers.count(numbers[i])
        if k > 1:
            numbers[i] = str(numbers[i])*k
    return set(numbers)

main()