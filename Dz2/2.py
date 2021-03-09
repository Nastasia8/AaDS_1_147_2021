def asd():
    a = ["tiger","leopard","elephant","Fox","wolf","camel","raccoon"]
    b = a[0]
    a[0] = a[6]
    a[6] = b
    print(a)
asd()