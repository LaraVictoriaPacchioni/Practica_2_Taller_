def convertir_a_segundos(duracion):
    """Convierte una duración en formato m:ss a segundos."""
    partes = duracion.split(":")
    minutos = int(partes[0])
    segundos = int(partes[1])

    return minutos * 60 + segundos


def convertir_a_minutos_segundos(total_segundos):
    """Convierte una cantidad total de segundos a minutos y segundos."""
    minutos = total_segundos // 60
    segundos = total_segundos % 60

    return minutos, segundos


def calcular_duracion_total(playlist):
    """Calcula la duración total de la playlist en segundos."""
    total_segundos = 0

    for cancion in playlist:
        total_segundos += convertir_a_segundos(cancion["duration"])

    return total_segundos


def obtener_cancion_mas_larga(playlist):
    """Devuelve la canción más larga de la playlist."""
    cancion_mas_larga = playlist[0]
    mayor_duracion = convertir_a_segundos(cancion_mas_larga["duration"])

    for cancion in playlist:
        duracion_actual = convertir_a_segundos(cancion["duration"])

        if duracion_actual > mayor_duracion:
            mayor_duracion = duracion_actual
            cancion_mas_larga = cancion

    return cancion_mas_larga


def obtener_cancion_mas_corta(playlist):
    """Devuelve la canción más corta de la playlist."""
    cancion_mas_corta = playlist[0]
    menor_duracion = convertir_a_segundos(cancion_mas_corta["duration"])

    for cancion in playlist:
        duracion_actual = convertir_a_segundos(cancion["duration"])

        if duracion_actual < menor_duracion:
            menor_duracion = duracion_actual
            cancion_mas_corta = cancion

    return cancion_mas_corta