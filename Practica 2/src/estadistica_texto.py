def obtener_lineas(texto):
    """Retorna una lista de las lineas del texto."""
    return texto.split("\n")
def contar_lineas(lineas):
    """Retorna la cantidad de líneas."""
    return len(lineas)
def contar_palabras(lineas):
    """Retorna la cantidad total de palabras."""
    total = 0

    for linea in lineas:
        palabras = linea.split()
        total += len(palabras)

    return total
def calcular_promedio(cantidad_palabras, cantidad_lineas):
    """Retorna el promedio de palabras por línea."""
    return cantidad_palabras / cantidad_lineas
def lineas_mayores_promedio(lineas, promedio):
    """Imprime las líneas con más palabras que el promedio."""

    print("Líneas por encima del promedio:")

    for linea in lineas:
        cantidad = len(linea.split())

        if cantidad > promedio:
            print("-", linea)
def main():
    texto = "Esto es una prueba"

    lineas = obtener_lineas(texto)
    cantidad_lineas = contar_lineas(lineas)
    cantidad_palabras = contar_palabras(lineas)
    promedio = calcular_promedio(cantidad_palabras, cantidad_lineas)

    print("Total de líneas:", cantidad_lineas)
    print("Total de palabras:", cantidad_palabras)
    print("Promedio de palabras por línea:", promedio)

    lineas_mayores_promedio(lineas, promedio)


if __name__ == "__main__":
    main()
