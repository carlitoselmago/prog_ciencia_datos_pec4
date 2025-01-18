import unittest

# Descubre y ejecuta todos los tests encontrados en la carpeta "test"
if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.discover("test", pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

# REF: https://docs.python.org/3/library/unittest.html