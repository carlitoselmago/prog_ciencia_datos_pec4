import pandas as pd
from helpers import helpers

class ejercicio():
    name = "Ejercicio1"
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

    def main(self, dataset_uri:str = 'data/dataset.csv', valores:int = 5) -> pd.DataFrame:
        """
        Carga y visualización inicial del dataset
        """
        df = pd.read_csv(dataset_uri, delimiter=";")
        if self.verbose:
            self.helpers.print_msg(f'El dataframe {dataset_uri} contiene las {valores} primeras filas : \n\n {self.helpers.pandas_print(df.head(valores))}')

            self.helpers.print_msg(f'En la prueba participaron {df.size} ciclistas')

            self.helpers.print_msg(f'El datframe contiene las siguientes columnas {list(df.columns)}')

        return df


if __name__ == "__main__":
    ex1 = ejercicio(verbose = 1)
    ex1.main()