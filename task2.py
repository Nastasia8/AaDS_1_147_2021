def main():
    funk()



def funk():
    diction = ['tiger', 'leopad', 'elephaint', 'Fox', 'wolf', 'camel','raccon']
    removed = diction.pop(0)
    diction.insert(0, 'raccon')
    removed = diction.pop(6)
    diction.insert(6, 'tiger')
    print(diction)





main()