def main():
    funk()



def funk():
    diction = [3, 8, 2, 1, 4, 7, 5, 6, 10, 9]
    new_dict = []

    for i in diction:
        if i%2 == 0:
            new_dict.append(i)
    print(new_dict)




main()