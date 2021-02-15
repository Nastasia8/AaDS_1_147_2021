from  random import randint

def main():
    slov()

def slov():
    a = ("Crime and Punishment", 1, 331, 1866, "The Master and Margarita", 1, 470, 1966, "War and Peace", 4, 1274, 1869, "And Quiet Flows the Don", 4, 1600, 1940)
    dct = {}
   
    for v in a:
        dct_one = dct.fromkeys(a, randint(0,1000))
    print(dct_one)

  

main()