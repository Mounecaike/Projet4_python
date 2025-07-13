class Round :
    def __init__(self, name, start_time, end_time, matches) :
      self.name = name
      self.start_time = start_time
      self.end_time = end_time
      self.matches = []

    def end_round(self, end_time):
      self.end_time = end_time
      


    def to_dict(self):
      return {
          "name": self.name,
          "start_time": self.start_time,
          "end_time": self.end_time,
          "matches": self.matches
      }
    @classmethod
    def from_dict(cls, data):
        return cls (
            data["name"],
            data["start_time"],
            data["end_time"],
            data["matches"]
        )