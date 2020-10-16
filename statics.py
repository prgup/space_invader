class Stat():
	def __init__(self, setg):
		self.setg = setg
		self.active_game = False
		with open('highscore.txt') as file:
			self.high_score = int(file.read()) if file else 0
		self.reset_stats()

	def reset_stats(self):
		self.ships_left = self.setg.ships_limit
		self.score = 0
		self.level = 1
