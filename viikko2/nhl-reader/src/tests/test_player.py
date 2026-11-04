import unittest

from player import Player, PlayerStats


class StubReader:
    def __init__(self, players):
        self.players = players

    def get_players(self):
        return self.players


def create_player(name, nationality, team, goals, assists):
    return Player({
        "name": name,
        "nationality": nationality,
        "assists": assists,
        "goals": goals,
        "team": team,
        "games": 10,
        "id": name,
    })


class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        players = [
            create_player("Finn", "FIN", "DAL", 20, 30),
            create_player("Swede", "SWE", "DAL", 30, 10),
            create_player("Finn Two", "FIN", "BOS", 10, 15),
            create_player("Finn Three", "FIN", "DAL", 5, 5),
        ]
        self.stats = PlayerStats(StubReader(players))

    def test_reader_players_are_used(self):
        self.assertEqual(len(self.stats.players), 4)

    def test_top_scorers_by_nationality_filters_and_sorts_by_points(self):
        result = self.stats.top_scorers_by_nationality("FIN")

        self.assertEqual([player.name for player in result], ["Finn", "Finn Two", "Finn Three"])

    def test_top_scorers_by_team_filters_and_sorts_by_points(self):
        result = self.stats.top_scorers_by_team("DAL")

        self.assertEqual([player.name for player in result], ["Finn", "Swede", "Finn Three"])

    def test_top_goal_scorers_returns_requested_number_in_goal_order(self):
        result = self.stats.top_goal_scorers(2)

        self.assertEqual([player.name for player in result], ["Swede", "Finn"])

    def test_unknown_filter_returns_no_players(self):
        self.assertEqual(self.stats.top_scorers_by_team("NYR"), [])
        self.assertEqual(self.stats.top_scorers_by_nationality("CAN"), [])


if __name__ == "__main__":
    unittest.main()
