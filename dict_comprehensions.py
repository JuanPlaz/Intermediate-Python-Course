from cmath import sqrt


def run():
    """my_dict = {}    

    for i in range(1,101):      ##Crear diccionario que almacene como llave un numero y como valor el numero al cubo. 
        if i % 3 != 0:          ##Solo los numeros que no sean divisibles por 3
            my_dict[i] = i**3 
        ##my_dict.update({i:i*i})
    """
    myDict = {i : i**3 for i in range(1,101) if i % 3 != 0}
    print(myDict)

    dict2 = {i : sqrt(i) for i in range(1,1001)}
    print(dict2)



if __name__ == '__main__':
    run()