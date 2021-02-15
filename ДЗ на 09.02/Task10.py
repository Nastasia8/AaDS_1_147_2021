def pow(y,z):
    res = " "
    nums = range(1,21)
    for i in nums:
        i = i**y**z
        print(i)
y = int(input("Укажите значение y: \n"))
z = int(input("Укажите значение z: \n"))
pow(y,z)