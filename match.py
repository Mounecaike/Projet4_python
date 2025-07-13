class Match :
    def __init__(self, player1, player2, score1, score2) :
      self.player1 = player1
      self.player2 = player2
      self.score1 = score1
      self.score2 = score2

    def set_result(self, score1, score2):
      self.score1 = score1
      self.score2 = score2

    def to_dict(self):
      return {
          "player1": self.player1,
          "player2": self.player2,
          "score1": self.score1,
          "score2": self.score2,
      }
    @classmethod
    def from_dict(cls, data) :
      return cls (
          data["player1"],
          data["player2"],
          data["score1"],
          data["score2"]
      )
