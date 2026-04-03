def tiene_un_solo_arroba(email):
    """Devuelve True si el email contiene exactamente un arroba."""
    return email.count("@") == 1


def tiene_texto_antes_del_arroba(email):
    """Devuelve True si hay al menos un carácter antes del arroba."""
    posicion_arroba = email.find("@")
    return posicion_arroba > 0


def tiene_punto_despues_del_arroba(email):
    """Devuelve True si hay al menos un punto después del arroba."""
    posicion_arroba = email.find("@")
    parte_despues_arroba = email[posicion_arroba + 1:]

    return "." in parte_despues_arroba


def no_empieza_ni_termina_mal(email):
    """Devuelve True si no empieza ni termina con arroba o punto."""
    if email.startswith("@") or email.startswith("."):
        return False

    if email.endswith("@") or email.endswith("."):
        return False

    return True


def dominio_valido(email):
    """Devuelve True si después del último punto hay al menos 2 caracteres."""
    posicion_ultimo_punto = email.rfind(".")
    parte_final = email[posicion_ultimo_punto + 1:]

    return len(parte_final) >= 2


def es_email_valido(email):
    """Devuelve True si el email cumple todos los criterios pedidos."""
    return (
        tiene_un_solo_arroba(email)
        and tiene_texto_antes_del_arroba(email)
        and tiene_punto_despues_del_arroba(email)
        and no_empieza_ni_termina_mal(email)
        and dominio_valido(email)
    )