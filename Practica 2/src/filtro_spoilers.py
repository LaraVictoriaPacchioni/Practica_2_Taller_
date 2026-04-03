def pedir_spoilers():
    """Pide al usuario las palabras spoiler separadas por coma."""
    entrada = input("Ingrese las palabras spoiler (separadas por coma): ")
    palabras = entrada.split(",")

    spoilers = []

    for palabra in palabras:
        spoilers.append(palabra.strip())

    return spoilers


def crear_reemplazo(palabra):
    """Devuelve una cadena de asteriscos del mismo largo que la palabra."""
    return "*" * len(palabra)


def reemplazar_una_palabra(texto, palabra):
    """Reemplaza una palabra por asteriscos sin distinguir mayúsculas."""
    texto_resultado = ""
    i = 0
    palabra_minuscula = palabra.lower()
    largo_palabra = len(palabra)

    while i < len(texto):
        fragmento = texto[i:i + largo_palabra]

        if fragmento.lower() == palabra_minuscula:
            texto_resultado += crear_reemplazo(palabra)
            i += largo_palabra
        else:
            texto_resultado += texto[i]
            i += 1

    return texto_resultado


def filtrar_spoilers(texto, spoilers):
    """Reemplaza todas las palabras spoiler del texto por asteriscos."""
    texto_filtrado = texto

    for spoiler in spoilers:
        if spoiler != "":
            texto_filtrado = reemplazar_una_palabra(texto_filtrado, spoiler)

    return texto_filtrado