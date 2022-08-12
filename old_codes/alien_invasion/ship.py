import pygame
class Ship:
	"""A class for the ship"""
	def __init__(self, ai_game):
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		#loading the ship image
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		#start each new ship at the bottom centre
		self.rect = [600, 650]
		# Movement flag
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Update the ship's position based on the movement flag."""
		if self.moving_right and self.rect[0] < 1200:
			self.rect[0] += 1
		if self.moving_left and self.rect[0] > 0:
			self.rect[0] -= 1


	def blitme(self):
		"""draw the ship at its current location"""
		self.screen.blit(self.image, self.rect)

