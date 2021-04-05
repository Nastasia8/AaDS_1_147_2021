def main():
    feb()

def feb():
    f0=0
    f1=1
    print(f0)
    print(f1)
    for n in range(1,14):
        f1 = f1 + f0
        f0 = f1 - f0
        print(f1)
    

main()
