import pygame

class BG():
	def __init__(self, screen):
		self.screen = screen
		self.image = pygame.image.load("images/bg4.jpg")
		self.image1 = pygame.image.load("images/bgg.jpg")

		self.rect = self.image.get_rect()
		self.rect1 = self.image1.get_rect()
		self.rect_scrn = self.screen.get_rect()
		self.rect.centerx = self.rect_scrn.centerx
		self.rect1.centerx = self.rect_scrn.centerx


	def show(self):
		self.screen.blit(self.image, self.rect)
	def show1(self):
		self.screen.blit(self.image1, self.rect1) 
 
