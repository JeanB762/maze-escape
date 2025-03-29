import pygame
from src.Config import PLAYER_SIZE

class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/player.png")
        self.image = pygame.transform.scale(self.image, (PLAYER_SIZE, PLAYER_SIZE))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 4

    def move(self, dx, dy, maze):
        new_rect = self.rect.move(dx, dy)
        if not maze.collides(new_rect):
            self.rect = new_rect

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
