"""Simulación de competencia de cocina y ranking."""

ROUNDS = [
    {
        "theme": "Entrada",
        "scores": {
            "Valentina": {"judge_1": 8, "judge_2": 7, "judge_3": 9},
            "Mateo": {"judge_1": 7, "judge_2": 8, "judge_3": 7},
            "Camila": {"judge_1": 9, "judge_2": 9, "judge_3": 8},
            "Santiago": {"judge_1": 6, "judge_2": 7, "judge_3": 6},
            "Lucía": {"judge_1": 8, "judge_2": 8, "judge_3": 8},
        },
    },
    {
        "theme": "Plato principal",
        "scores": {
            "Valentina": {"judge_1": 9, "judge_2": 9, "judge_3": 8},
            "Mateo": {"judge_1": 8, "judge_2": 7, "judge_3": 9},
            "Camila": {"judge_1": 7, "judge_2": 6, "judge_3": 7},
            "Santiago": {"judge_1": 9, "judge_2": 8, "judge_3": 8},
            "Lucía": {"judge_1": 7, "judge_2": 8, "judge_3": 7},
        },
    },
    {
        "theme": "Postre",
        "scores": {
            "Valentina": {"judge_1": 7, "judge_2": 8, "judge_3": 7},
            "Mateo": {"judge_1": 9, "judge_2": 9, "judge_3": 8},
            "Camila": {"judge_1": 8, "judge_2": 7, "judge_3": 9},
            "Santiago": {"judge_1": 7, "judge_2": 7, "judge_3": 6},
            "Lucía": {"judge_1": 9, "judge_2": 9, "judge_3": 9},
        },
    },
    {
        "theme": "Cocina internacional",
        "scores": {
            "Valentina": {"judge_1": 8, "judge_2": 9, "judge_3": 9},
            "Mateo": {"judge_1": 7, "judge_2": 6, "judge_3": 7},
            "Camila": {"judge_1": 9, "judge_2": 8, "judge_3": 8},
            "Santiago": {"judge_1": 8, "judge_2": 9, "judge_3": 7},
            "Lucía": {"judge_1": 7, "judge_2": 7, "judge_3": 8},
        },
    },
    {
        "theme": "Final libre",
        "scores": {
            "Valentina": {"judge_1": 9, "judge_2": 8, "judge_3": 9},
            "Mateo": {"judge_1": 8, "judge_2": 9, "judge_3": 8},
            "Camila": {"judge_1": 7, "judge_2": 7, "judge_3": 7},
            "Santiago": {"judge_1": 9, "judge_2": 9, "judge_3": 9},
            "Lucía": {"judge_1": 8, "judge_2": 8, "judge_3": 7},
        },
    },
]

def initialize_stats(rounds):
    """Retorna un diccionario con las estadisticas acumuladas."""
    participantes = rounds[0]["scores"].keys()
    stats = {}

    for participante in participantes:
        stats[participante] = {
            "total_score": 0,
            "rounds_won": 0,
            "best_round": 0,
            "rounds_played": 0,
        }

    return stats

def calculate_round_score(puntajes_jueces):
    """Retorna el total de puntos de una ronda de un participante."""
    return sum(puntajes_jueces.values())

def get_round_winner(puntajes_ronda):
    """Obtiene el ganador de la ronda."""
    ganador = max(puntajes_ronda, key=puntajes_ronda.get)
    puntaje = puntajes_ronda[ganador]
    return ganador, puntaje

def update_stats(stats, puntajes_ronda):
    """Actualiza las estadisticas acumuladas."""
    for participante, puntaje in puntajes_ronda.items():
        stats[participante]["total_score"] += puntaje
        stats[participante]["rounds_played"] += 1

        if puntaje > stats[participante]["best_round"]:
            stats[participante]["best_round"] = puntaje

def add_round_win(stats, ganador):
    """Aumenta numero de rondas jugadas por el ganador."""
    stats[ganador]["rounds_won"] += 1

def build_ranking(stats):
    """ ranking ordenado por el puntaje total ordenado descendentemente."""
    ranking = []

    for participante, datos in stats.items():
        ranking.append(
            {
                "name": participante,
                "total_score": datos["total_score"],
                "rounds_won": datos["rounds_won"],
                "best_round": datos["best_round"],
                "average": datos["total_score"] / datos["rounds_played"],
            }
        )

    ranking.sort(key=lambda item: item["total_score"], reverse=True)
    return ranking


def print_round_table(num_ronda, tema, ganador, puntaje, ranking):
    """Imprime el resultado de una ronda y la tabla de rondas."""
    print(f"Ronda {num_ronda} - {tema}:")
    print(f"Ganador/a: {ganador} ({puntaje} pts)")
    print()

    print("Tabla de posiciones:")
    print(
        f"{'Cocinero':<12}"
        f"{'Puntaje':>10}"
        f"{'Rondas ganadas':>18}"
        f"{'Mejor ronda':>15}"
        f"{'Promedio':>12}"
    )
    print("-" * 67)

    for fila in ranking:
        print(
            f"{fila['name']:<12}"
            f"{fila['total_score']:>10}"
            f"{fila['rounds_won']:>18}"
            f"{fila['best_round']:>15}"
            f"{fila['average']:>12.1f}"
        )

    print("\n")

def print_final_table(ranking):
    """Imprimo la tabla final de rankings."""
    print("Tabla de posiciones final:")
    print(
        f"{'Cocinero':<12}"
        f"{'Puntaje':>10}"
        f"{'Rondas ganadas':>18}"
        f"{'Mejor ronda':>15}"
        f"{'Promedio':>12}"
    )
    print("-" * 67)

    for fila in ranking:
        print(
            f"{fila['name']:<12}"
            f"{fila['total_score']:>10}"
            f"{fila['rounds_won']:>18}"
            f"{fila['best_round']:>15}"
            f"{fila['average']:>12.1f}"
        )



def run_competition():
    """Ejecuta la competicion e imprime todas las rondas de la tabla."""
    stats = initialize_stats(ROUNDS)

    for num_ronda, datos_ronda in enumerate(ROUNDS, start=1):
        puntajes_ronda = {}

        for participante, puntajes_jueces in datos_ronda["scores"].items():
            puntajes_ronda[participante] = calculate_round_score(puntajes_jueces)

        update_stats(stats, puntajes_ronda)

        ganador, puntaje = get_round_winner(puntajes_ronda)
        add_round_win(stats, ganador)

        ranking = build_ranking(stats)

        print_round_table(
            num_ronda,
            datos_ronda["theme"],
            ganador,
            puntaje,
            ranking,
        )

    ranking_final = build_ranking(stats)
    print_final_table(ranking_final)
if __name__ == "__main__":
    run_competition()
