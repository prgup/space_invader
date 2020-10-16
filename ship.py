import pygame

class Ship():
	def __init__(self, screen, settings):
		self.screen = screen
		self.right = False
		self.left  = False
		self.setg=  settings

		self.image = pygame.image.load("images/shipf.png")
		self.rect = self.image.get_rect()
		self.rect_scrn = self.screen.get_rect()

		self.rect.centerx = self.rect_scrn.centerx
		self.rect.bottom = self.rect_scrn.bottom - 5
		self.center = float(self.rect.centerx)
		
	def reset_it(self):
		self.rect.centerx = self.rect_scrn.centerx
		self.center = float(self.rect.centerx)
 

	def update(self):
		if self.right and self.rect.right < self.rect_scrn.right:
			self.center += self.setg.speed_factor
			#two if commond is necessity here
		if self.left and self.rect.left > 0:
			self.center -= self.setg.speed_factor
		
		self.rect.centerx = self.center

	def show(self):
		self.screen.blit(self.image, self.rect) 

