import unittest
import pandas as pd
from ejercicio2 import ejercicio
from ejercicio1 import ejercicio as ejercicio1

class TestEjercicio2(unittest.TestCase):

    # Creamos un dataframe de prueba común
    datatest=  {
            "dorsal": [1, 2, 3],
            "biker": ["Perico", "Palotes","Jaimito"],
            "club": ["sants","lescorts","sants"],
            "time": ["01:30:00", "02:00:00", "00:00:00"],

        }

    def test_name_surname(self):
        """
        Verifica que la función name_surname() anonimiza correctamente los nombres.
        """
        
        df = pd.DataFrame(self.datatest)

        # Creamos una instancia de ejercicio2
        instance = ejercicio(verbose=False)

        # Ejecutamos name_surname
        df_anon=instance.name_surname(df)

        # Verificamos que los nombres se reemplazan
        self.assertNotEqual(list(df_anon["biker"]), ["Perico", "Palotes","Jaimito"])
        self.assertEqual(len(df_anon), len(df))  

    def test_main(self):
        """
        Verifica que la función main() elimina correctamente los ciclistas con tiempo "00:00:00".
        """
        
        df = pd.DataFrame(self.datatest)

        # Creamos una instancia de ejercicio2
        instance = ejercicio(verbose=False)

        # Ejecutamos la función main
        df_cleaned = instance.main(df)

        # Verificamos que los ciclistas con tiempo "00:00:00" fueron eliminados
        self.assertNotIn("00:00:00", df_cleaned["time"].values)
        self.assertLess(len(df_cleaned), len(df))  # Deben haber menos filas en el DataFrame

if __name__ == "__main__":
    unittest.main()
