def function(Numbers):
    dict = {}
    m = []
    for number in Numbers:
        if number in dict:
            dict[number] += 1
        else:
            dict[number] = 1
        if dict[number] == 1:
            m.append(number)
        else:
            i = 1
            num = number
            while i != dict[number]:
                num = num*10+number
                i += 1
            m.append(str(num))
    m = set(m)
    print(m)


Numbers = [1, 7, 4, 7, 15, 4, 7, 5, 2]
function(Numbers)
