import pygame
from src.config import TILE_SIZE, BLACK, RED, MAZE_LAYOUT

class Item:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)

    def draw(self, screen):
        pygame.draw.circle(screen, RED, self.rect.center, TILE_SIZE // 3)

class Maze:
    def __init__(self):
        self.walls = []
        self.items = []

        for row_idx, row in enumerate(MAZE_LAYOUT):
            for col_idx, cell in enumerate(row):
                x, y = col_idx * TILE_SIZE, row_idx * TILE_SIZE
                if cell == "1":
                    self.walls.append(pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))
                elif cell == "2":
                    self.items.append(Item(x + TILE_SIZE // 4, y + TILE_SIZE // 4))

    def draw(self, screen):
        for wall in self.walls:
            pygame.draw.rect(screen, BLACK, wall)
        for item in self.items:
            item.draw(screen)

    def collides(self, rect):
        return any(rect.colliderect(wall) for wall in self.walls)
