import unittest

from statistics_service import StatisticsService, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89),
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_returns_matching_player(self):
        player = self.stats.search("Semenko")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Semenko")
        self.assertEqual(player.team, "EDM")

    def test_search_matches_substring(self):
        player = self.stats.search("Kurr")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Kurri")

    def test_search_returns_first_matching_player(self):
        player = self.stats.search("e")
        self.assertEqual(player.name, "Semenko")

    def test_search_returns_none_when_no_match(self):
        self.assertIsNone(self.stats.search("Selänne"))

    def test_team_returns_all_players_of_that_team(self):
        edm = self.stats.team("EDM")
        self.assertEqual(len(edm), 3)
        self.assertEqual(
            sorted(p.name for p in edm),
            ["Gretzky", "Kurri", "Semenko"],
        )

    def test_team_with_single_player(self):
        pit = self.stats.team("PIT")
        self.assertEqual(len(pit), 1)
        self.assertEqual(pit[0].name, "Lemieux")

    def test_team_with_unknown_name_returns_empty_list(self):
        self.assertEqual(self.stats.team("NYR"), [])

    def test_top_returns_players_sorted_by_points_by_default(self):
        top = self.stats.top(2)
        self.assertEqual(len(top), 3)
        self.assertEqual(top[0].name, "Gretzky")
        self.assertEqual(top[1].name, "Lemieux")
        self.assertEqual(top[2].name, "Yzerman")

    def test_top_zero_returns_the_best_player(self):
        top = self.stats.top(0)
        self.assertEqual(len(top), 1)
        self.assertEqual(top[0].name, "Gretzky")

    def test_top_returns_every_player_when_asked_for_enough(self):
        top = self.stats.top(4)
        self.assertEqual(len(top), 5)
        self.assertEqual(top[-1].name, "Semenko")

    def test_top_sorts_by_goals(self):
        top = self.stats.top(4, SortBy.GOALS)
        self.assertEqual(
            [p.name for p in top],
            ["Lemieux", "Yzerman", "Kurri", "Gretzky", "Semenko"],
        )

    def test_top_sorts_by_assists(self):
        top = self.stats.top(4, SortBy.ASSISTS)
        self.assertEqual(
            [p.name for p in top],
            ["Gretzky", "Yzerman", "Lemieux", "Kurri", "Semenko"],
        )
