def nombre_valido(nombre):
    """Devuelve True si el nombre no es nulo, vacío ni solo espacios."""
    if nombre is None:
        return False

    if nombre.strip() == "":
        return False

    return True


def nota_valida(nota):
    """Devuelve True si la nota no es nula, vacía y es numérica."""
    if nota is None:
        return False

    if nota == "":
        return False

    return nota.isdigit()


def normalizar_nombre(nombre):
    """Devuelve el nombre sin espacios extra y en formato título."""
    return nombre.strip().title()


def normalizar_estado(estado):
    """Devuelve el estado en formato título."""
    return estado.strip().title()


def limpiar_registro(registro):
    """Devuelve un registro limpio y normalizado."""
    return {
        "name": normalizar_nombre(registro["name"]),
        "grade": int(registro["grade"]),
        "status": normalizar_estado(registro["status"]),
    }


def filtrar_registros_validos(students):
    """Devuelve una lista con los registros válidos y normalizados."""
    registros_validos = []

    for registro in students:
        nombre = registro["name"]
        nota = registro["grade"]

        if nombre_valido(nombre) and nota_valida(nota):
            registros_validos.append(limpiar_registro(registro))

    return registros_validos


def eliminar_duplicados(registros):
    """
    Elimina duplicados por nombre, conservando el registro con la nota más alta.
    """
    registros_sin_duplicados = {}

    for registro in registros:
        nombre = registro["name"]

        if nombre not in registros_sin_duplicados:
            registros_sin_duplicados[nombre] = registro
        else:
            if registro["grade"] > registros_sin_duplicados[nombre]["grade"]:
                registros_sin_duplicados[nombre] = registro

    return list(registros_sin_duplicados.values())


def ordenar_por_nombre(registros):
    """Devuelve los registros ordenados alfabéticamente por nombre."""
    return sorted(registros, key=lambda registro: registro["name"])


def normalizar_registros(students):
    """Devuelve la lista final de registros limpios."""
    registros_validos = filtrar_registros_validos(students)
    registros_sin_duplicados = eliminar_duplicados(registros_validos)
    registros_ordenados = ordenar_por_nombre(registros_sin_duplicados)

    return registros_ordenados