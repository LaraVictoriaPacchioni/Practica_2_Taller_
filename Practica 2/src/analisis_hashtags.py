def extraer_hashtags(post):
    """Devuelve una lista con los hashtags de una publicación."""
    palabras = post.split()
    hashtags = []

    for palabra in palabras:
        if palabra.startswith("#"):
            hashtags.append(palabra)

    return hashtags


def contar_frecuencias(posts):
    """Devuelve un diccionario con la frecuencia de cada hashtag."""
    frecuencias = {}

    for post in posts:
        hashtags = extraer_hashtags(post)

        for hashtag in hashtags:
            if hashtag in frecuencias:
                frecuencias[hashtag] += 1
            else:
                frecuencias[hashtag] = 1

    return frecuencias


def obtener_trending(frecuencias):
    """Devuelve un diccionario con los hashtags que aparecen más de una vez."""
    trending = {}

    for hashtag, cantidad in frecuencias.items():
        if cantidad > 1:
            trending[hashtag] = cantidad

    return trending


def total_hashtags_unicos(frecuencias):
    """Devuelve la cantidad total de hashtags únicos."""
    return len(frecuencias)