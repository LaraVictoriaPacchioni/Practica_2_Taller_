def desplazar_caracter(caracter, desplazamiento):
    """Devuelve el carácter desplazado si es una letra."""
    if caracter.isupper():
        base = ord("A")
        posicion = ord(caracter) - base
        nueva_posicion = (posicion + desplazamiento) % 26
        return chr(base + nueva_posicion)

    if caracter.islower():
        base = ord("a")
        posicion = ord(caracter) - base
        nueva_posicion = (posicion + desplazamiento) % 26
        return chr(base + nueva_posicion)

    return caracter


def cifrar_mensaje(mensaje, desplazamiento):
    """Devuelve el mensaje cifrado con César."""
    mensaje_cifrado = ""

    for caracter in mensaje:
        mensaje_cifrado += desplazar_caracter(caracter, desplazamiento)

    return mensaje_cifrado


def descifrar_mensaje(mensaje_cifrado, desplazamiento):
    """Devuelve el mensaje original a partir del cifrado."""
    return cifrar_mensaje(mensaje_cifrado, -desplazamiento)