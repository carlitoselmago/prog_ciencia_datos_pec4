from helpers import helpers
from ejercicio1 import ejercicio as ex1
from ejercicio2 import ejercicio as ex2
import os


class ejercicio():
    name = "Ejercicio3"
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

    def minutes_002040(self,time_str):
        """
        Redondea strings de tiempo a múltiplos de 20min en formato hh:mi
        """
        hours, minutes, seconds = map(int, time_str.split(":"))

        #Redondeamos los minutos en el múltiplo de 20 más cercano
        rounded_minutes = (minutes // 20) * 20
        # Devolvemos el valor con el formato hh:mi
        return f"{hours:02}:{rounded_minutes:02}"



    def main(self, df):
        """
        Agrupación de tiempos de llegada en intervalos
        """
        df["time_grouped"] = df["time"].apply(self.minutes_002040)
        if self.verbose:
            self.helpers.print_msg(f'Mostramos los 15 primeros ciclistas después de crear la nueva columna time_grouped: \n\n {self.helpers.pandas_print(df.head(15))}')

        agrupados_df = df.groupby("time_grouped").size().reset_index(name="count")

        # Generamos el histograma
        if self.verbose:
            self.helpers.plot_hist(
                X=agrupados_df["time_grouped"],
                Y=agrupados_df["count"],
                nombre_archivo = "histograma", 
                titulo="Distribución de ciclistas por tiempo de llegada",
                labelx="Time Group (hh:mm)",
                labely="Numero de ciclistas"
                )

        return df

if __name__ == "__main__":
    ex1 = ex1()
    ex2 = ex2()
    ex3 = ejercicio(verbose = True)
    ex3.main(ex2.main(ex1.main()))