import math
def main():
    funk(5,2)


def funk(m,k):
    t = 2 * math.pi * math.sqrt(m / k)
    v = 2 * math.pi / t
    print(v)
    print(t)

main()