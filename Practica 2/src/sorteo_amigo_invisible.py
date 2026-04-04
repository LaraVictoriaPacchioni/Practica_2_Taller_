import random


def obtener_participantes(entrada):
    """Devuelve una lista de participantes sin espacios extra."""
    partes = entrada.split(",")
    participantes = []

    for parte in partes:
        nombre = parte.strip()

        if nombre != "":
            participantes.append(nombre)

    return participantes


def hay_minimo_participantes(participantes):
    """Devuelve True si hay al menos 3 participantes."""
    return len(participantes) >= 3


def hay_duplicados(participantes):
    """Devuelve True si hay nombres duplicados ignorando mayúsculas y espacios."""
    vistos = set()

    for participante in participantes:
        nombre_normalizado = participante.strip().lower()

        if nombre_normalizado in vistos:
            return True

        vistos.add(nombre_normalizado)

    return False


def asignacion_valida(participantes, asignados):
    """Devuelve True si nadie se asignó a sí mismo."""
    for i in range(len(participantes)):
        if participantes[i] == asignados[i]:
            return False

    return True


def sortear_amigo_invisible(participantes):
    """Devuelve un diccionario con el sorteo de amigo invisible."""
    asignados = participantes[:]

    while True:
        random.shuffle(asignados)

        if asignacion_valida(participantes, asignados):
            break

    sorteo = {}

    for i in range(len(participantes)):
        sorteo[participantes[i]] = asignados[i]

    return sorteo