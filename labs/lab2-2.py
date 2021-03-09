animals = ["tiger", "leopard", " elephant", "Fox", "wolf", "camel", "raccoon"]

def change(a):
    a[0], a[-1] = a[-1], a[0]
    return a