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

    def filtar_por_club(self, df, club:str = ""):
        return df[df["club_clean"] == club]

    def mejor_tiempo(self,df):
        df = df.sort_values(by=["time"], ascending=True).reset_index(drop=True)
        return df.head(1)
    
    def posicion_global(self,df,ciclista):
        # Reseteamos el índice del dataframe para actualizarl los índices
        df_reset = df.reset_index(drop=True)
        ciclista = df_reset.loc[df_reset.eq(ciclista.iloc[0]).all(axis=1)]

        # Obtenemos el índice global del mejor ciclista de UCSC
        posicion = ciclista.index[0]

        return posicion
    
    def porcentaje_posicion(self,df, posicion):
        df_reset = df.reset_index(drop=True)
        posicion_percent = (df_reset.index.get_loc(posicion) / len(df_reset)) * 100

        return posicion_percent

    def main(self,df):
        
        # Filtramos por el club
        UCSC_df = self.filtar_por_club(df, "UCSC")

        # Obtenemos el ciclista con el mejor tiempo
        mejor_tiempo = self.mejor_tiempo(UCSC_df)

        posicion = self.posicion_global(df, mejor_tiempo )
        
        # Obtenemos la posición en porcentaje
        posicion_percent = self.porcentaje_posicion(df,posicion)

        if self.verbose:
            self.helpers.print_msg(f'Mostramos los ciclistas de la UCSC (Unió Ciclista Sant Cugat): \n\n {self.helpers.pandas_print(UCSC_df)}')

            self.helpers.print_msg(f'El ciclista de la UCSC que ha obtenido el mejor tiempo es: \n\n {mejor_tiempo["biker"].values[0]} con {mejor_tiempo["time"].values[0]}')

            self.helpers.print_msg(f'El mismo ciclista quedó en la posición #{posicion} global. Siendo de los {posicion_percent:.2f}% mejores resultados.')

        return df

if __name__ == "__main__":

    ex1 = ex1()
    ex2 = ex2()
    ex3 = ex3()
    ex4 = ex4()
    ex5 = ejercicio(verbose = True)
    ex5.main(ex4.main(ex3.main(ex2.main(ex1.main()))))