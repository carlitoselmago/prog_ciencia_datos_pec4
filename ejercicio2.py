from helpers import helpers
from faker import Faker
import pandas as pd
from ejercicio1 import ejercicio as ex1

class ejercicio():
    name = "Ejercicio2"
    verbose = False
    
    def __init__(self,verbose:bool = False):
        """
        Verbose controla si las funciones de las clase deben imprimir sus resultados
        poner como True para que imprima los resultados y False para que no lo haga
        """
        self.verbose = verbose
        self.helpers = helpers()
        if self.verbose:
            self.helpers.print_cabecera(self.name)

    def name_surname(self, df : pd.DataFrame, loc = 'es_ES'):
        # Creamos un objeto Faker con una localización de España
        fake = Faker('es_ES')
        df["biker"] = [fake.name() for n in df["biker"]]
        return df

    def main(self, df):
        """
        Anonimización de nombres de los ciclistas
        """
        # Anonimizamos los nombres
        df = self.name_surname(df)
        if self.verbose:
            self.helpers.print_msg(f'Listado de los 5 primeros ciclistas con nombre anonimizado \n\n {self.helpers.pandas_print(df.head(5))}')
        
        # Eliminamos los ciclistas con tiempo 00:00:00
        ciclistas_original = df.size
        df = df[df["time"] != "00:00:00"]
        if self.verbose:
            self.helpers.print_msg(f'Se han eliminado {ciclistas_original - df.size} ciclistas que no participaron en la prueba')

            self.helpers.print_msg(f'El dataframe contiene ahora {df.size} ciclistas, mostramos los 5 primeros: \n\n {self.helpers.pandas_print(df.head(5))}')

            self.helpers.print_msg(f'Los ciclistas con dorsal #1000 son: \n\n {self.helpers.pandas_print(df[df["dorsal"] == 1000])}')

        return df

if __name__ == "__main__":
    ex1 = ex1()
    ex2 = ejercicio(verbose = True)
    ex2.main(ex1.main())