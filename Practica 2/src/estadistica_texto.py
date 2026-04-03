def obtener_lineas(texto):
    """Devuelve una lista con las líneas del texto."""
    return texto.splitlines()


def contar_palabras_linea(linea):
    """Devuelve la cantidad de palabras de una línea."""
    return len(linea.split())


def contar_lineas(lineas):
    """Devuelve la cantidad total de líneas."""
    return len(lineas)


def contar_palabras(lineas):
    """Devuelve la cantidad total de palabras."""
    total = 0

    for linea in lineas:
        total += contar_palabras_linea(linea)

    return total


def calcular_promedio(cantidad_palabras, cantidad_lineas):
    """Devuelve el promedio de palabras por línea."""
    return cantidad_palabras / cantidad_lineas


def obtener_lineas_superiores(lineas, promedio):
    """Devuelve las líneas cuya cantidad de palabras supera el promedio."""
    superiores = []

    for linea in lineas:
        if contar_palabras_linea(linea) > promedio:
            superiores.append(linea)

    return superiores
