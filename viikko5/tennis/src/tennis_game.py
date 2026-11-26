class TennisGame:
    SCORE_NAMES = ("Love", "Fifteen", "Thirty", "Forty")
    ENDGAME_SCORE = 4

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self._tied_score()
        if self._is_end_game():
            return self._end_game_score()
        return self._mid_game_score()

    def _tied_score(self):
        if self.player1_score < 3:
            return f"{self.SCORE_NAMES[self.player1_score]}-All"
        else:
            return "Deuce"

    def _is_end_game(self):
        return self.player1_score >= self.ENDGAME_SCORE or self.player2_score >= self.ENDGAME_SCORE

    def _end_game_score(self):
        score_difference = self.player1_score - self.player2_score
        if score_difference == 1:
            return f"Advantage {self.player1_name}"
        elif score_difference == -1:
            return f"Advantage {self.player2_name}"
        elif score_difference >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def _mid_game_score(self):
        return f"{self.SCORE_NAMES[self.player1_score]}-{self.SCORE_NAMES[self.player2_score]}"
