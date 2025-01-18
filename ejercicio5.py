from helpers import helpers
from ejercicio1 import ejercicio as ex1
from ejercicio2 import ejercicio as ex2
from ejercicio3 import ejercicio as ex3
from ejercicio4 import ejercicio as ex4

class ejercicio():
    name = "Ejercicio5"
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

    def main(self,df):
        
        UCSC_df = df[df["club_clean"] == "UCSC"]
        mejor_tiempo = UCSC_df.head(1)
        
        # Reseteamos el índice del dataframe para actualizarlo después de haber borrado los ciclistas con tiempo 0:00:00
        df_reset = df.reset_index(drop=True)
        ciclista = df_reset.loc[df_reset.eq(mejor_tiempo.iloc[0]).all(axis=1)]

        # Obtenemos el índice global del mejor ciclista de UCSC
        posicion = ciclista.index[0]

        # Obtenemos la posición en porcentaje
        posicion_percent = (df_reset.index.get_loc(posicion) / len(df_reset)) * 100

        if self.verbose:
            self.helpers.print_msg(f'Mostramos los ciclistas de la UCSC (Unió Ciclista Sant Cugat): \n\n {self.helpers.pandas_print(UCSC_df)}')

            self.helpers.print_msg(f'El ciclista de la UCSC que ha obtenido el mejor tiempo es: \n\n {mejor_tiempo["biker"].values[0]} con {mejor_tiempo["time"].values[0]}')

            self.helpers.print_msg(f'El mismo ciclista quedó en la posición #{posicion} global. Siendo de los {posicion_percent:.2f}% mejores resultados.')

        return df_reset

if __name__ == "__main__":

    ex1 = ex1()
    ex2 = ex2()
    ex3 = ex3()
    ex4 = ex4()
    ex5 = ejercicio(verbose = True)
    ex5.main(ex4.main(ex3.main(ex2.main(ex1.main()))))