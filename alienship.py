import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
	def __init__ (self, screen, settings):
		super(Alien, self).__init__()#python 2.7 syntax
		self.screen= screen
		self.setg  = settings
		self.image =  pygame.image.load('images/aliens1.png')
		self.rect = self.image.get_rect()
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		self.screen_rect = self.screen.get_rect()

	def update(self):
		self.x1 = float(self.rect.x)
		self.x1 += (self.setg.alien_across_factor*
			self.setg.fleet_direcn)
		self.rect.x = self.x1
		#self.rect.x will take integar value only

	def check_edge_contact(self):
		if self.rect.right >= self.screen_rect.right:
			return True
		elif self.rect.left <=0:
			return True


	def show(self):
		self.screen.blit(self.image, self.rect)



