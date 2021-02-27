 ##создать функцию НОК(а,b)
#def HOK(a,b):
#    #a1= a
#    #b1= b
#    while a != 0 and b != 0:
#        if a > b:
#            a = a % b 
#        else:
#            b = b % a
#            return HOD//a+b
#print("HOK({0};{1}) = {2}".format(a,b, ((a*b)/HOD)))

#a = int(input('Input 1 number:'))
#b = int(input('Input 2 number:'))
#HOK(a, b)
def HOK(x, y):

      if x > y:
              max = x
      else:
              max = y

      while(True):
              if((max % x == 0) and (max % y == 0)):
                      HOK = max
                      break
              max += 1

      return HOK

num1 = int("54")
num2 = int("24")

print("The HOK of", num1,"and", num2,"is", HOK(num1, num2))

