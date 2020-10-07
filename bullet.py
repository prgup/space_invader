import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self, screen, setting, ship):
		super().__init__()
		self.screen = screen
		self.setg = setting
		# Create a bullet rect
		self.rect = pygame.Rect(0,0, 
			self.setg.bull_width,self.setg.bull_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		self.y = float(self.rect.y)

	def update(self):
		"""Move the bullet up the screen."""
		self.y -= self.setg.bull_speed
		self.rect.y = self.y

	def show(self):
		pygame.draw.rect(self.screen, 
			self.setg.bull_color, self.rect )


