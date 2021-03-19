def main():
    y = int(input())
    z = int(input())
    calc(y,z)

def calc(y,z):
    
    for i in range(1,21,2):
        print(i**y**z, end="")


main() 
