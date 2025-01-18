import unittest
import pandas as pd
from ejercicio1 import ejercicio

class TestEjercicio(unittest.TestCase):

    def test_main(self):
        """
        Verifica que la función main() devuelve un DataFrame de pandas.
        """
        # Creamos una instancia de ejercicio
        instance = ejercicio(verbose=False)

        # Ejecutamos la función main
        df = instance.main(dataset_uri='data/dataset.csv')

        # Verificamos que el resultado es un DataFrame
        self.assertIsInstance(df, pd.DataFrame)

        # Verificamos que el DataFrame tiene mas columnas y filas que 0
        self.assertGreater(len(df), 0, "El DataFrame no tiene filas.")
        self.assertGreater(len(df.columns), 0, "El DataFrame no tiene columnas.")

if __name__ == "__main__":
    unittest.main()
