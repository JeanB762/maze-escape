import pygame
from src.config import TILE_SIZE, BLUE

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
        self.speed = 4

    def move(self, dx, dy, maze):
        new_rect = self.rect.move(dx, dy)
        if not maze.collides(new_rect):
            self.rect = new_rect

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, self.rect)
