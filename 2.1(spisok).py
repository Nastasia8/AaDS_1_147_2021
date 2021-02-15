
# def fan( list_a ):
#     new_list = []
#     for number in list_a:
#         if number %2 == 0:
#             new_list.append(number)
#     print(new_list)

##########################################

# print([num for num in a if num %2 == 0])
#a = [3, 8, 2, 1, 4, 7, 5, 6 ,10, 9]
#fan(a)

##########################################

def fan(number):
    return number %2 == 0

a = list(range(1, 11))
print(list(filter(fan, a)))   
##########################################


