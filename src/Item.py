import pygame

from src.Config import ACHIEVEMENT_SIZE

class Item:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/achievements.png")
        self.image = pygame.transform.scale(self.image, (ACHIEVEMENT_SIZE, ACHIEVEMENT_SIZE))
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)