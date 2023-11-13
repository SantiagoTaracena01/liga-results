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

# Módulo random para generar resultados.
import random
import numpy as np

# Función simulate_match que simula un partido y retorna el resultado.
def simulate_match(local, visitor, local_goal_advantage, visitor_goal_disadvantage, local_accuracy_advantage, visitor_accuracy_disadvantage, penalty_foul_probability, corner_goal_probability):

    # Calcula los goles para cada equipo en función de los tiros y penales.
    local_goals = 0
    visitor_goals = 0

    # Cálculo de la efectividad de los tiros al arco para cada equipo.
    local_shooting_accuracy = local.shots_on_target_accuracy
    visitor_shooting_accuracy = visitor.shots_on_target_accuracy

    # Cálculo de la efectividad de los penales para cada equipo.
    local_penalty_accuracy = local.penalty_accuracy
    visitor_penalty_accuracy = visitor.penalty_accuracy

    # Cálculo del número de tiros para cada equipo.
    local_shots = round((np.random.normal(local.shots_on_target, 1) * local_goal_advantage))
    visitor_shots = round((np.random.normal(visitor.shots_on_target, 1) * visitor_goal_disadvantage))

    # Ciclo que verifica cuántos tiros locales acaban en gol.
    for _ in range(local_shots):
        if (random.random() < (local_shooting_accuracy + local_accuracy_advantage)):
            local_goals += 1

    # Ciclo que verifica cuántos tiros visitantes acaban en gol.
    for _ in range(visitor_shots):
        if (random.random() < (visitor_shooting_accuracy + visitor_accuracy_disadvantage)):
            visitor_goals += 1

    # Cálculo del número de penales para cada equipo.
    local_penalties = round(np.random.normal((local.penalties * 10), 1))
    visitor_penalties = round(np.random.normal((visitor.penalties * 10), 1))

    # Probabilidad de que haya una falta de penal en el partido.
    if (random.random() < penalty_foul_probability):

        # Penales a cobrar por el equipo local.
        for _ in range(local_penalties):
            if (random.random() < local_penalty_accuracy):
                local_goals += 1

        # Penales a cobrar por el equipo visitante.
        for _ in range(visitor_penalties):
            if (random.random() < visitor_penalty_accuracy):
                visitor_goals += 1

    # Cálculo del número de corners para cada equipo.
    local_corners = round((np.random.normal(local.corners, 1) * local_goal_advantage))
    visitor_corners = round((np.random.uniform(visitor.corners, 1) * visitor_goal_disadvantage))

    # Corners a cobrar por el equipo local.
    for _ in range(local_corners):
        if (random.random() < corner_goal_probability):
            local_goals += 1

    # Corners a cobrar por el equipo visitante.
    for _ in range(visitor_corners):
        if (random.random() < corner_goal_probability):
            visitor_goals += 1

    # Simulación de tarjetas amarillas y rojas.
    local_yellow_cards = round(np.random.normal(local.cards_per_game, 1))
    visitor_yellow_cards = round(np.random.normal(visitor.cards_per_game, 1))
    local_red_cards = round(np.random.normal((local_yellow_cards * local.red_cards_per_card), 1))
    visitor_red_cards = round(np.random.normal((visitor_yellow_cards * visitor.red_cards_per_card), 1))

    # Ajuste del resultado si un equipo tiene un jugador expulsado.
    if (local_red_cards > 0):
        visitor_goals += local_red_cards
    if (visitor_red_cards > 0):
        local_goals += visitor_red_cards

    # Retorno del marcador del partido.
    return (local_goals, visitor_goals)
