import pygame

from src.Config import TILE_SIZE, MAZE_LAYOUT_5
from src.Item import Item

class Maze:
    def __init__(self):
        self.walls = []
        self.items = []

        self.wall_image = pygame.image.load("assets/wall.png")
        self.wall_image = pygame.transform.scale(self.wall_image, (TILE_SIZE, TILE_SIZE))

        self.floor_image = pygame.image.load("assets/floor.png")
        self.floor_image = pygame.transform.scale(self.floor_image, (TILE_SIZE, TILE_SIZE))

        self.layout = MAZE_LAYOUT_5

        for row_idx, row in enumerate(self.layout):
            for col_idx, cell in enumerate(row):
                x, y = col_idx * TILE_SIZE, row_idx * TILE_SIZE
                if cell == "1":
                    self.walls.append(pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))
                elif cell == "2":
                    self.items.append(Item(x + TILE_SIZE // 4, y + TILE_SIZE // 4))

    def draw(self, screen):
        for row_idx, row in enumerate(self.layout):
            for col_idx, cell in enumerate(row):
                x, y = col_idx * TILE_SIZE, row_idx * TILE_SIZE
                screen.blit(self.floor_image, (x, y))

        for wall in self.walls:
            screen.blit(self.wall_image, (wall.x, wall.y))

        for item in self.items:
            item.draw(screen)

    def collides(self, rect):
        return any(rect.colliderect(wall) for wall in self.walls)
