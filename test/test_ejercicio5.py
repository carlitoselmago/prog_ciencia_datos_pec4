import unittest
import pandas as pd
from ejercicio5 import ejercicio

class TestEjercicio5(unittest.TestCase):

    # Creamos un DataFrame de prueba común
    datatest=  {
            "dorsal": [1, 2, 3],
            "biker": ["Palotes","Jaimito","Perico"],
            "club_clean": ["SANTSENSE","SANTSENSE","HUESCA"],
            "time": ["06:29:40", "06:59:40","06:19:40"]
    }

    def test_filtrar_por_club(self):
        """
        Verifica que la función filtrar_por_club() filtra correctamente por nombre de club.
        """
        instance = ejercicio(verbose=False)

        df = pd.DataFrame(self.datatest)

        # Filtrar por club
        result = instance.filtar_por_club(df, "SANTSENSE")

        # Verificar que solo quedan filas del club 
        self.assertTrue((result["club_clean"] == "SANTSENSE").all())
        self.assertEqual(len(result), 2)

    def test_mejor_tiempo(self):
        """
        Verifica que la función mejor_tiempo() devuelve el ciclista con el menor tiempo.
        """
        instance = ejercicio(verbose=False)

        df = pd.DataFrame(self.datatest)

        # Obtener el mejor tiempo
        result = instance.mejor_tiempo(df)

        # Verificar que es Palotes
        self.assertEqual(result.iloc[0]["biker"], "Perico")
        self.assertEqual(result.iloc[0]["time"], "06:19:40")

    def test_posicion_global(self):
        """
        Verifica que la función posicion_global() devuelve la posición correcta en el DataFrame original.
        """
        instance = ejercicio(verbose=False)

        df = pd.DataFrame(self.datatest)

        mejor_tiempo = df[df["biker"] == "Perico"]

        # Obtenemos la posición global
        posicion = instance.posicion_global(df, mejor_tiempo)

        # Verificamos que la posición global es la correcta
        self.assertEqual(posicion, 2)

    def test_porcentaje_posicion(self):
        """
        Verifica que la función porcentaje_posicion() calcula correctamente el porcentaje de la posición.
        """
        instance = ejercicio(verbose=False)
        df = pd.DataFrame(self.datatest)

        # Calcular el porcentaje de la posición
        posicion = 1
        porcentaje = instance.porcentaje_posicion(df, posicion)

        # Verificar el porcentaje
        self.assertAlmostEqual(porcentaje,33.33333333333333, places=2)

if __name__ == "__main__":
    unittest.main()
