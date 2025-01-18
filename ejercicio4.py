from helpers import helpers
from ejercicio1 import ejercicio as ex1
from ejercicio2 import ejercicio as ex2
from ejercicio3 import ejercicio as ex3
import re


class ejercicio():
    name = "Ejercicio4"
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

    def clean_club(self,club):

        # Convertimos a mayúsculas
        club = club.upper()
        
        # Eliminamos las palabras genéricas
        lista_negra = [
            'PEÑA CICLISTA ', 'PENYA CICLISTA ', 'AGRUPACIÓN CICLISTA ', 'AGRUPACION CICLISTA ',
            'AGRUPACIÓ CICLISTA ', 'AGRUPACIO CICLISTA ', 'CLUB CICLISTA ', 'CLUB '
        ]
        for phrase in lista_negra:
            club = club.replace(phrase, '')
        
        # Eliminamos los prefijos
        prefijos = r"^(C\.C\. |C\.C |CC |C\.D\. |C\.D |CD |A\.C\. |A\.C |AC |A\.D\. |A\.D |AD |A\.E\. |A\.E |AE |E\.C\. |E\.C |EC |S\.C\. |S\.C |SC |S\.D\. |S\.D |SD )"
        club = re.sub(prefijos, '', club)
        
        # Eliminamos los sufijos
        sufijos = r"( T\.T\.| T\.T| TT| T\.E\.| T\.E| TE| C\.C\.| C\.C| CC| C\.D\.| C\.D| CD| A\.D\.| A\.D| AD| A\.C\.| A\.C| AC)$"
        club = re.sub(sufijos, '', club)
        
        # Eliminamos espacio en blanco al principio y final del nombre del club
        club = club.strip()
        
        return club

    def main(self,df):
        df["club_clean"] = df["club"].apply(self.clean_club)
        if self.verbose:
            self.helpers.print_msg(f'Mostramos los 15 primeros ciclistas después de crear la nueva columna club_clean: \n\n {self.helpers.pandas_print(df.head(15))}')

        # Agrupamos los ciclistas por nombre de club
        agrupados_clubs = df.groupby("club_clean").size().reset_index(name="count")
        
        # Los ordenamos por cantidad de miembros
        agrupados_clubs = agrupados_clubs.sort_values(by="count", ascending=False)
        
        # Para poder visualizarlo escogemos la cantidad de los clubes más grandes
        top = 10

        agrupados_clubs_top = agrupados_clubs.head(top)

        if self.verbose:
            self.helpers.print_msg(f'Mostramos los clubes por orden de inscritos: \n\n {self.helpers.pandas_print(agrupados_clubs_top)}')

            self.helpers.plot_hist(
                X = agrupados_clubs_top["club_clean"][1:],
                Y = agrupados_clubs_top["count"][1:],
                nombre_archivo = "histograma_clubs", 
                titulo=f"Distribución de ciclistas por los {top} clubes más grandes (sin incluir Independientes )",
                labelx="Club",
                labely="Numero de ciclistas"
                )
            
        return df

if __name__ == "__main__":

    ex1 = ex1()
    ex2 = ex2()
    ex3 = ex3()
    ex4 = ejercicio(verbose = True)
    ex4.main(ex3.main(ex2.main(ex1.main())))


# REF:
# https://www.w3schools.com/python/python_regex.asp