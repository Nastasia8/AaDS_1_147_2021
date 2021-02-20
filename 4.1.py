# # # numbers =[1,-5,0,9,-17]
# # # print({number:"+" if number >0 else "-" if number<0 else "zero" for number in numbers})
# # def NOD(x,y):
# #     a=x
# #     b=y
# #     while x!=0 and y!=0:
# #         if x>y:
# #             x=x % y
# #         else:
# #             y=y % x 
# #     
# #     print("NOD({0};{1}) = {2}".format(a, b, (x+y)))

# # x=int(input("x="))
# # y=int(input("y="))
# # NOD(x,y)

# def NOK(x,y):
#     c=x*y
#     while x!=0 and y!=0:
#         if x>y:
#             x=x % y
#         else:
#             y=y % x 
#     return c//(x+y)

# x=int(input("x="))
# y=int(input("y="))
# n=NOK(x,y)
# print("NOK({0};{1}) = {2}".format(x, y, n))

a=[[4,3,5,1],[0,7,2,9],[2,6,3,8]]
print("Before:")
for num in range (len(a)):
    print(a[num])
print("After:")
for num in range(len(a)):
    print(a[num][::-1])

b=[[13,97,56],[17,23,85],[22,45,66]]
print("Before:")
for num in range (len(b)):
    print(b[num])
print("After:")
for num in range(len(b)):
    print(b[num][::-1])