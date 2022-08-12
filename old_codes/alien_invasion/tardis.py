import pygame
class Tardis:
	"""A class for the ship"""
	def __init__(self, ai_game):
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		#loading the ship image
		self.image = pygame.image.load('images/tardis.bmp')
		self.rect = self.image.get_rect()
		#start each new ship at the bottom centre
		self.rect = (600, 400)

	def blitme(self):
		"""draw the ship at its current location"""
		self.screen.blit(self.image, self.rect)

