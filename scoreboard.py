import pygame.font
from pygame.sprite import Group
from lives import Lives
class Scoreboard():
	def __init__(self, screen, setg, stats ):
		self.screen = screen
		self.screen_rect  =self.screen.get_rect()
		self.setg = setg
		self.stats = stats
		self.txt_color = (30,30,30)
		self.font = pygame.font.SysFont(None, 36)
		self.width = 0
		self.prep_scrn()
		self.prep_highscrn()
		#self.prep_level()
		self.prep_lives()

	def prep_lives(self):
		self.lives = Group()
		for i in range(self.stats.ships_left):
			live = Lives(self.screen)
			live.rect.x = 10 + i*live.rect.width
			live.rect.top = 10
			self.lives.add(live)
		live = Lives(self.screen)
		self.width = live.rect.width*self.stats.ships_left




	def prep_level(self):
		str_level = ' / ' + str(self.stats.level)
		self.level_img = self.font.render(str_level
			, True, self.txt_color, self.setg.bg_color)
		self.level_rect = self.level_img.get_rect()
		self.level_rect.left = self.width + 10
		#self.level_rect.left =  self.screen_rect.left + 20
		self.level_rect.top = 10 


	def prep_scrn(self):
		round_score = int(round(self.stats.score, -1))
		score_value = '{:,}'.format(round_score)
		self.score_img = self.font.render(score_value
			, True, self.txt_color, self.setg.bg_color)
		self.score_rect = self.score_img.get_rect()
		self.score_rect.centerx =  self.screen_rect.centerx
		self.score_rect.top = 10 

	def prep_highscrn(self):
		round_score = int(round(self.stats.high_score, -1))
		score_value = '{:,}'.format(round_score)
		self.score1_img = self.font.render(score_value
			, True, self.txt_color, self.setg.bg_color)
		self.score1_rect = self.score1_img.get_rect()
		self.score1_rect.right =  self.screen_rect.right - 20
		self.score1_rect.top = 10 


	def show(self):
		self.screen.blit(self.score_img, self.score_rect)
		self.screen.blit(self.score1_img, self.score1_rect)
		self.screen.blit(self.level_img, self.level_rect)
		self.lives.draw(self.screen)


 	