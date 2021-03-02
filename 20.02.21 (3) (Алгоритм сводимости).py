x=int(input("Введите X: "))
def fun(x):
  while x!=1:
        if x%2==0:
            x=x//2
        else:
            x=x*3
            x=x+1
            x=x//2
        print(x, end=" ")

fun(x)


