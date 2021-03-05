#задача1
def nod(x, y):
    while y:
        x, y = y, x % y
    return x
x = int(input("введите значение x:"))
y = int(input("введите значение y:"))

print ("НОД =", nod(x, y))



#задача2
x = int(input("введите значение x:"))
y = int(input("введите значение y:"))

def nod(x, y):
    while y:
        x, y = y, x % y
    return x
 
nok=(x*y)/nod(x,y)

print ("НОД =", nod(x, y))
print ("НОК =", nok)



#задача3
a=int(input("введите a:"))

def fun(a):

  while a!=1:
        if a%2==0:
            a=a//2
        else:
            a=a*3
            a=a+1
            a=a//2
        print(a, end=" ")

fun(a)



#задача4(a)
matrix = [[4, 3, 5, 1],[0, 7, 2, 9],[2, 6, 3, 8]]
print(matrix[0])
print(matrix[1])
print(matrix[2])

matrix[0][0] = 1 
matrix[0][1] = 5
matrix[0][2] = 3
matrix[0][3] = 4

matrix[1][0] = 9
matrix[1][1] = 2
matrix[1][2] = 7
matrix[1][3] = 0

matrix[2][0] = 8
matrix[2][1] = 3
matrix[2][2] = 6
matrix[2][3] = 2
     
print(" ")
print(matrix[0])
print(matrix[1])
print(matrix[2])



#задача 4 (б)
matr = [[13,96,56],[17,23,85],[22,45,66]]

print(matr[0])
print(matr[1])
print(matr[2])

x, y = 0, 2

for i in matr:
    i[x], i[y] = i[y], i[x]

print(" ")
print(matr[0])
print(matr[1])
print(matr[2])



#задача7

sp1=["Clematis", "Dahlia", "Rose", "Chrysanthemum", "Freesia", "Lily", "Peony"]
sp2=["tiger", "leopard", "elephant", "camel", "fox", "wolf", "raccoon"]
sp3=["Bass", "Roach", "Catfish", "Trout", "Mackerel",  "Anchovy"]

def func (sp1,simb):
  max=0
  newsp=[]

  for i in sp1:         
    if len(i)>max:
      max=len(i)

  for i in sp1:
    if len(i)<max:          
      a=max-len(i)          
      i=i+(simb*a)        
      newsp.append(i)
    else:
      newsp.append(i)
  print(newsp)

func(sp1,"#")
func(sp2,"#")
func(sp3,"#")