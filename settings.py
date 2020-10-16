class Setting():
	def __init__(self):
		self.scr_width = 660
		self.scr_height = 700
		self.bg_color = 0,0,0
		self.bull_height = 20
		self.bull_width =  5 #5
		self.bull_color = 200,200,200#55,55,55
		self.ships_limit = 3
		self.bull_limit = 3
		self.speed_multiple = 1.1
		self.score_multiple = 1.5
		self.initial_speed()

	def initial_speed(self):
		self.speed_factor = 2.5 #ship speed factor
		self.bull_speed = 1 #normal is 1 pixle 
		self.alien_across_factor = 1#1#1
		self.fleet_drop_factor = 10#1#10
		self.fleet_direcn = 1 #+1 for right-1 for left
		self.hit_point = 50
		
	def progressive_speed(self):
		self.speed_factor *= self.speed_multiple
		self.bull_speed *= self.speed_multiple #normal is 1 pixle 
		self.alien_across_factor *= self.speed_multiple
		self.fleet_drop_factor *= self.speed_multiple
		self.hit_point = int(self.hit_point*self.score_multiple)
		self.bull_limit += 1


