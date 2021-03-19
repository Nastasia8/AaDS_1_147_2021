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



#задача4(a)(можно сделать проще и приравнять нужные значения)
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



#задача 4 (б)(тут уже более адекватный второй способ)
matrix = [[13,96,56],[17,23,85],[22,45,66]]

print(matrix[0])
print(matrix[1])
print(matrix[2])

x, y = 0, 2

for i in matrix:
    i[x], i[y] = i[y], i[x]

print(" ")
print(matrix[0])
print(matrix[1])
print(matrix[2])



#задача 5 ОКАЗАЛАСЬ СЛИШКОМ СЛОЖНОЙ
#задача 6 АНАЛОГИЧНО ПЯТОЙ



#задача7
#пометки делаю для себя, потому что три часа пыталась понять где ошибка

spisok1=["Clematis", "Dahlia", "Rose", "Chrysanthemum", "Freesia", "Lily", "Peony"]
spisok2=["tiger", "leopard", "elephant", "camel", "fox", "wolf", "raccoon"]
spisok3=["Bass", "Roach", "Catfish", "Trout", "Mackerel",  "Anchovy"]

def func (spisok1,simvol):
  max=0
  newspisok=[]

  for i in spisok1:         #тут определяем самое длинное слово в списке и его длину записываем в max
    if len(i)>max:
      max=len(i)

  for i in spisok1:
    if len(i)<max:          #если индекс последней буквы меньше найденного максимума, тогда заходим в цикл
      a=max-len(i)          #из максимума вычитаем индекс последней буквы и записываем в а, чтобы знать сколько сиволов нужно добавить
      i=i+(simvol*a)        
      newspisok.append(i)
    else:
      newspisok.append(i)
  print(newspisok)

func(spisok1,"#")
func(spisok2,"#")
func(spisok3,"#")