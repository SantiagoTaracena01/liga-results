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

class Team(object):
    def __init__(self, team_data):
        self.name = team_data["name"]
        self.goals_per_game = team_data["goals_per_game"]
        self.shots_on_target = team_data["shots_on_target"]
        self.shots_on_target_accuracy = team_data["shots_on_target_accuracy"]
        self.penalties = team_data["penalties"]
        self.penalty_accuracy = team_data["penalty_accuracy"]
        self.corners = team_data["corners"]
        self.fouls_received_per_game = team_data["fouls_received_per_game"]
        self.offsides_per_game = team_data["offsides_per_game"]
        self.goals_per_game_received = team_data["goals_per_game_received"]
        self.shots_on_target_received = team_data["shots_on_target_received"]
        self.fouls_committed_per_game = team_data["fouls_committed_per_game"]
        self.recoveries_per_game = team_data["recoveries_per_game"]
        self.cut_passes_per_game = team_data["cut_passes_per_game"]
        self.entries_per_game = team_data["entries_per_game"]
        self.clears_per_game = team_data["clears_per_game"]
        self.cards_per_game = team_data["cards_per_game"]
        self.yellow_cards_per_card = team_data["yellow_cards_per_card"]
        self.red_cards_per_card = team_data["red_cards_per_card"]
