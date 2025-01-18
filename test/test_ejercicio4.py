import unittest
import pandas as pd
from ejercicio4 import ejercicio

class TestEjercicio4(unittest.TestCase):

    def test_clean_club(self):
        """
        Verifica que la función clean_club() limpia correctamente los nombres de los clubes.
        """
        instance = ejercicio(verbose=False)

        # Casos de prueba
        self.assertEqual(instance.clean_club("C.C. Huesca"), "HUESCA")
        self.assertEqual(instance.clean_club("Club Ciclista Sariñena"), "SARIÑENA")
        self.assertEqual(instance.clean_club("Peña Ciclista Santsense T.T."), "SANTSENSE")


    def test_main(self):
        """
        Verifica que la función main() añade la columna club_clean correctamente.
        """
        # Creamos un DataFrame de prueba
        datatest=  {
            "dorsal": [1, 2, 3],
            "biker": ["Perico", "Palotes","Jaimito"],
            "club": ["C.C. Huesca","Club Ciclista Sariñena","Peña Ciclista Santsense T.T."],
            "time": ["06:19:40", "06:29:40", "06:59:40"],

        }
        df = pd.DataFrame(datatest)

        # Creamos una instancia de ejercicio4
        instance = ejercicio(verbose=False)

        # Ejecutamos la función main
        df_result = instance.main(df)

        # Verificamos que la columna club_clean fue añadida
        self.assertIn("club_clean", df_result.columns)

        # Verificamos los valores de la columna club_clean
        expected_club_clean = ["HUESCA", "SARIÑENA", "SANTSENSE"]
        self.assertListEqual(list(df_result["club_clean"]), expected_club_clean)

if __name__ == "__main__":
    unittest.main()
