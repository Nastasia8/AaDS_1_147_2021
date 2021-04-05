y = int(input())
z = int(input())

def calc(y,z):
    for i in range(1,21,2):
        print(i**y**z)
calc(y,z)