class Stat():
	def __init__(self, setg):
		self.setg = setg
		self.active_game = False
		self.high_score = 0
		self.reset_stats()

	def reset_stats(self):
		self.ships_left = self.setg.ships_limit
		self.score = 0
		self.level = 1
