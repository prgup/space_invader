import pygame
from pygame.sprite import Sprite
class Lives(Sprite):
	def __init__(self, screen):
		super().__init__()
		self.screen = screen
		self.image = pygame.image.load('images/rocket.png')
		self.rect  =self.image.get_rect()
#variable name should be image 