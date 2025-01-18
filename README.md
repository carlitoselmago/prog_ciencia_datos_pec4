# prog_ciencia_datos_pec4

## Descripción
Este proyecto contiene una serie de ejercicios de programación que realizan cálculos y análisis sobre un dataset de una competición de ciclistas en Huesca. Los ejercicios se dividen en cinco módulos independientes, cada uno con un propósito específico:

1. **Ejercicio 1**: Carga y visualización inicial del dataset.
2. **Ejercicio 2**: Anonimización de nombres de los ciclistas.
3. **Ejercicio 3**: Agrupación de tiempos de llegada en intervalos.
4. **Ejercicio 4**: Limpieza y normalización de los nombres de los clubes ciclistas.
5. **Ejercicio 5**: Análisis del mejor ciclista por tiempo y su posición global en la competición.

Cada módulo puede ejecutarse de manera individual o a través del archivo principal `main.py`, que ejecuta todos los ejercicios en secuencia.

## Instalación

Instala las dependencias necesarias con:
```bash
pip install -r requirements.txt
```

## Ejecución

### Ejecutar todos los ejercicios

Para ejecutar todos los ejercicios utiliza el archivo `main.py`:
```bash
python main.py
```

### Ejecutar ejercicios individuales

 Cada ejercicio puede ejecutarse de manera independiente. Por ejemplo:
```bash
python ejercicio1.py
python ejercicio2.py
```

## Tests

Se incluye un conjunto de tests utilizando la librería `unitttest` . Los test se encuentran en la carpeta `test`.

### Ejecutar todos los tests

Para ejecutar todas los tests con un solo comando:
```bash
python run_all_tests.py
```

## Compatibilidad
Este proyecto ha sido testeado en:
- Windows 11
- Linux Fedora 38


### NOTA:

He utilizado clases para cada ejercicio. Empecé haciéndolo solo como archivos con funciones pero quería añadir una variable global dentro de cada clase (verbose) que me facilitara el mostrar resultados por terminal o no, según si la clase se ejecutaba dentro de otra clase y me parecía que hacerlo con clases era la forma más elegante o *pythonic* de hacerlo.  
Podría haber utilizado una estructura de clases más elegante en la que cada ejercicio fuera una subclase de una clase central "ejercicio" pero no quería alejarme demasiado del temario central de la asignatura/ejercicio.
