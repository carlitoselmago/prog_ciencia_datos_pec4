from ejercicio1 import ejercicio as ex1
from ejercicio2 import ejercicio as ex2
from ejercicio3 import ejercicio as ex3
from ejercicio4 import ejercicio as ex4
from ejercicio5 import ejercicio as ex5
 
if __name__ == "__main__":

    #Definimos una variable común para verbose
    v = True

    # Ejercicio1
    ex1 = ex1(verbose = v)
    df = ex1.main(dataset_uri = 'data/dataset.csv',valores = 5)

    # Ejercicio2
    ex2 = ex2(verbose = v)
    df = ex2.main(df)

    # Ejercicio3
    ex3 = ex3(verbose = v)
    df = ex3.main(df)

    # Ejercicio4
    ex4 = ex4(verbose = v)
    df = ex4.main(df)

    # Ejercicio5
    ex5 = ex5(verbose = v)
    df = ex5.main(df)
   