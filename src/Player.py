import pygame
from src.Config import PLAYER_SIZE

class Player:
    def __init__(self, x, y):
        self.image_player_right = pygame.image.load("assets/player_right.png")
        self.image_player_left = pygame.image.load("assets/player_left.png")
        
        self.image_player_right = pygame.transform.scale(self.image_player_right, (PLAYER_SIZE, PLAYER_SIZE))
        self.image_player_left = pygame.transform.scale(self.image_player_left, (PLAYER_SIZE, PLAYER_SIZE))

        self.image = self.image_player_right
        self.rect = self.image.get_rect(topleft=(x, y))
        self.direction = "right"
        self.speed = 4

    def move(self, dx, dy, maze):
        new_rect = self.rect.move(dx, dy)
        if not maze.collides(new_rect):
            self.rect = new_rect
            
            if dx > 0:
                self.direction = "right"
                self.image = self.image_player_right
            elif dx < 0:
                self.direction = "left"
                self.image = self.image_player_left

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
