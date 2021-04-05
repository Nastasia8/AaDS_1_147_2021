def change(input_set, input_list):
    for i in input_set:
        if i not in input_set:
            return False
        return True

print(change({1, 2, 'a', 4}, [5]))