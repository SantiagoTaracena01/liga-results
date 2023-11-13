"""
 * Universidad del Valle de Guatemala
 * (CC3039) Modelación y Simulación
 * Proyecto Final - Predicción de Resultados de Fútbol
 * 
 * Miembros del equipo de trabajo:
 * - Pedro Pablo Arriola Jiménez (20188)
 * - Marco Pablo Orozco Saravia (20857)
 * - Santiago Taracena Puga (20017)
"""

# Librerías necesarias para el desarrollo del proyecto.
import random
import pandas

# Módulos necesarios para el desarrollo del proyecto.
from utils.data import teams
from utils.classes.team import Team
from utils.simulate_match import simulate_match

# Diccionario que almacena los resultados.
results = { team["name"]: [0 for _ in range(8)] for team in teams }

# Equipos instanciados con las estadísticas investigadas.
instanced_teams = [Team(team) for team in teams]

"""
Lista de los stats: [Matches, Wins, Draws, Losses, GF, GA, GD, Pts]

0: Partidos jugados (siempre debe ser 38)
1: Partidos ganados
2: Partidos empatados
3: Partidos perdidos
4: Goles a favor
5: Goles en contra
6: Diferencia de goles (GF - GA)
7: Puntos acumulados
"""

# Iteraciones para la simulación de Montecarlo.
ITERATIONS = 10_000

# Ciclo for que ejecuta todas las iteraciones correspondientes a Montecarlo.
for _ in range(ITERATIONS):

    # Ciclos que iteran para jugar todos los partidos de cada jornada.
    for team in instanced_teams:
        for rival in instanced_teams:

            # Verificación de no ejecutar un partido entre el mismo equipo.
            if (team.name != rival.name):

                # Ventaja ligera por ser el equipo local.
                local_goal_advantage = random.uniform(1.1, 1.2)
                visitor_goal_disadvantage = random.uniform(0.02, 0.04)

                # Desventaja ligera por ser el equipo visitante.
                visitor_shoot_disadvantage = random.uniform(0.85, 0.95)
                visitor_accuracy_disadvantage = random.uniform(-0.02, -0.01)

                # Variables para dictar probabilidades extra de gol.
                penalty_foul_probability = random.uniform(0.05, 0.1)
                corner_goal_probability = random.uniform(0.01, 0.04)

                # Simulación del partido y obtención del resultado.
                score = simulate_match(team, rival, local_goal_advantage, visitor_shoot_disadvantage, visitor_goal_disadvantage, visitor_accuracy_disadvantage, penalty_foul_probability, corner_goal_probability)
                local_score, visitor_score = score

                # Equipos local y visitante.
                local_name = team.name
                visitor_name = rival.name

                # Aumento de los partidos jugados por cada uno.
                results[local_name][0] += 1
                results[visitor_name][0] += 1

                # Cambios en caso de victoria local.
                if (local_score > visitor_score):

                    # El equipo local aumenta un partido ganado y suma tres puntos.
                    results[local_name][1] += 1
                    results[visitor_name][3] += 1
                    results[local_name][7] += 3

                # Cambios en caso de victoria visitante.
                elif (local_score < visitor_score):

                    # El equipo visitante aumenta un partido ganado y suma tres puntos.
                    results[local_name][3] += 1
                    results[visitor_name][1] += 1
                    results[visitor_name][7] += 3

                # Cambios en caso de empate.
                else:

                    # Ambos equipos suman un punto y un partido empatado.
                    results[local_name][2] += 1
                    results[visitor_name][2] += 1
                    results[local_name][7] += 1
                    results[visitor_name][7] += 1

                # Aumento de goles a favor de ambos equipos.
                results[local_name][4] += local_score
                results[visitor_name][4] += visitor_score

                # Aumento de goles en contra de ambos equipos.
                results[local_name][5] += visitor_score
                results[visitor_name][5] += local_score

    # Cálculo de la diferencia de goles al finalizar la liga.
    for team in results:
        results[team][6] = (results[team][4] - results[team][5])

# Obtención de los resultados finales en promedio.
for team in results:
    for index, stat in enumerate(results[team]):
        results[team][index] = round((stat / ITERATIONS))

# Organización del diccionario por los puntos de cada equipo, y en segundo lugar por su diferencia de goles.
sorted_results = dict(sorted(
    results.items(),
    key=lambda team: (team[1][-1], team[1][-2]),
    reverse=True,
))

# Datos a colocar en un dataframe de pandas.
data = [[result, *results[result]] for result in sorted_results]

# Espacio incial para la impresión del dataset.
print("\n")

# Impresión del dataset.
dataset = pandas.DataFrame(data, columns=["Team", "Matches", "W", "D", "L", "GF", "GA", "GD", "Pts."])
dataset.index = range(1, (len(dataset) + 1))
print(dataset)

# Espacio final para la impresión del dataset.
print("\n")

# Almacenamiento de los resultados.
dataset.to_csv("./results/results.csv", index=False)
