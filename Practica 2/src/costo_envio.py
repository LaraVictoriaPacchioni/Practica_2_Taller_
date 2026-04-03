def zona_valida(zona):
    """Devuelve True si la zona ingresada es válida."""
    zonas_disponibles = ["local", "regional", "nacional"]
    return zona in zonas_disponibles


def obtener_categoria_peso(peso):
    """Devuelve la categoría según el peso del paquete."""
    if peso <= 1:
        return "hasta_1"
    if peso <= 5:
        return "entre_1_y_5"
    return "mas_de_5"


def calcular_costo_envio(peso, zona):
    """Devuelve el costo de envío según el peso y la zona."""
    costos = {
        "hasta_1": {
            "local": 500,
            "regional": 1000,
            "nacional": 2000,
        },
        "entre_1_y_5": {
            "local": 1000,
            "regional": 2500,
            "nacional": 4500,
        },
        "mas_de_5": {
            "local": 2000,
            "regional": 5000,
            "nacional": 8000,
        },
    }

    categoria = obtener_categoria_peso(peso)
    return costos[categoria][zona]