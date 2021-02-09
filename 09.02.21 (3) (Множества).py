def func(input_set,input_list):
     for i in input_list:
         if i not in input_set:
             return False
         return True
print (func({1,2,'a',4},[5]))
