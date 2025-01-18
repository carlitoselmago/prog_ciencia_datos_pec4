from tabulate import tabulate
import matplotlib.pyplot as plt
import os

class helpers():
    """
    Conjunto de funciones recurrentes para mostrar datos y enbellecimiento de datos en terminal
    """

    def __init__(self):
        pass

    def plot_hist(self,X,Y,nombre_archivo='histograma',titulo='Mi título',labelx='',labely='', mostrar=True, guardar=True):
        """
        Genera un gráfico matplotlib dados los vectores X e Y.
        Opcionalmente podemos mostrarlos y/o guardarlos en un archivo png
        """
        # Generamos el histograma con matplotlib
        plt.figure(figsize=(10, 6))
        plt.bar(X, Y)
        plt.title(titulo)
        plt.xlabel(labelx)
        plt.ylabel(labely)
        plt.grid(axis="y", linestyle="--", alpha=0.7)

        if guardar:
            output_path = os.path.join("img", f"{nombre_archivo.strip()}.png")
            plt.savefig(output_path)
        if  mostrar:
            plt.show()

    def print_msg(self,msg):
        """
        Imprime un mensaje con decoraciones para mayor legibilidad en terminal
        """
        print("****************************************************************")
        print(msg)
        print("****************************************************************")
        print("")

    def print_cabecera(self,msg):
        """
        Imprime una cabecera para separar cada ejercicio en terminal
        """
        print("")
        total_width = len(msg) + 52
        
        # linea superior
        print('╭' + '─' * total_width + '╮')
        
        # linea msg
        print('│ ' + msg.center(total_width - 2) + ' │')
        
        # linea inferior
        print('╰' + '─' * total_width + '╯')


    def pandas_print(self, dataframe) -> str:
        """
        Muestra un dataframe de pandas de una manera más legible
        """
        return tabulate(dataframe, headers='keys', tablefmt='psql')

# REF:
#https://www.datacamp.com/tutorial/python-tabulate