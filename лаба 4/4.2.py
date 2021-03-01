def main():
    nok()
    nok1()

def nok():
    print("Введите 2 числа для нахождения НОК")
    a = int(input())
    b = int(input())
    import math
    print("НОК:", a, b, "= ", ((a * b) // math.gcd(a, b)))
    
def nok1():
     print("Введите 2 числа для нахождения НОК 2 способом")
     c = int(input())
     d = int(input())
     while c != 0 and d != 0:
         if (c > d) and (c%d==0):
             c %= d
             sum = c + d
             nok2 = (d*c)/sum
             print("НОК", d, "и", c, "= ", nok2)  
        
        
       
         if (c<d) and (d%c==0): #nteger division or modulo by zero надо как-то пофиксить
             d %= c
             sum = d + c
             nok2 = (d*c)/sum
             print("НОК", d, "и", c, "= ", nok2) 
          

         else:
             print("нет общего делителя")
             print("нет нок")
     

    
      

      
main()