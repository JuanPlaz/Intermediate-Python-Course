def run():
    
    """my_list = []
    pow_list = []

    for i in range(1,101,1):
        my_list.append(i)

    for value in my_list:
        if value**2 % 3 == 0:
            continue
        else:
            pow_list.append(value*value)"""
    
    squares = [i**2 for i in range (1, 101) if i % 3 != 0]
    multiples = [i for i in range (1, 100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(multiples)




if __name__ == '__main__':
    run()