import unittest
import pandas as pd
from ejercicio3 import ejercicio

class TestEjercicio3(unittest.TestCase):

    # Creamos un dataframe de prueba común
    datatest=  {
            "dorsal": [1, 2, 3],
            "biker": ["Perico", "Palotes","Jaimito"],
            "club": ["sants","lescorts","sants"],
            "time": ["06:19:40", "06:29:40", "06:59:40"],

        }

    def test_minutes_002040(self):
        """
        Verifica que la función minutes_002040 redondea correctamente los minutos a múltiplos de 20.
        """
        instance = ejercicio(verbose=False)

        # Casos de prueba
        self.assertEqual(instance.minutes_002040("06:19:40"), "06:00")
        self.assertEqual(instance.minutes_002040("06:29:40"), "06:20")
       

    def test_main(self):
        """
        Verifica que la función main() añade la columna time_grouped correctamente.
        """
     
        df = pd.DataFrame(self.datatest)

        # Creamos una instancia de ejercicio3
        instance = ejercicio(verbose=False)

        # Ejecutamos la función main
        df_result = instance.main(df)

        # Verificamos que la columna time_grouped fue añadida
        self.assertIn("time_grouped", df_result.columns)

        # Verificamos los valores de la columna time_grouped
        expected_time_grouped = ["06:00", "06:20", "06:40"]
        self.assertListEqual(list(df_result["time_grouped"]), expected_time_grouped)

if __name__ == "__main__":
    unittest.main()
