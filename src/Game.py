import sys 
import pygame
from src.Config import WIDTH, HEIGHT, WHITE, FPS, BLACK, LEVELS, TILE_SIZE
from src.Player import Player
from src.Maze import Maze
from src.Menu import Menu
from src.Score import Score
from datetime import datetime
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Maze Escape")
        self.clock = pygame.time.Clock()
        self.running = True
        self.current_level = 0

        pygame.mixer.init()
        pygame.mixer.music.load("assets/background_music.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        self.item_sound = pygame.mixer.Sound("assets/achievement.mp3")

        self.menu = Menu(self.screen, self)
        self.maze = None
        self.player = None
        self.score = Score(self.screen)
        self.font = pygame.font.Font(None, 40)

    def run(self):
        """Inicia o loop principal do jogo."""
        while True:
            if self.menu.running:
                self.menu.handle_events()  
                self.menu.draw()  
            elif self.running:  
                self.start_new_game()

            self.clock.tick(FPS)

    def start_new_game(self):
        """Inicia um novo jogo."""
        self.current_level = 0
        self.maze = Maze(self.current_level)
        self.player = Player(TILE_SIZE, TILE_SIZE)
        self.running = True  
        self.game_loop()

    def game_loop(self):
        """Loop principal do jogo."""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
            
        if not self.running:  
            self.menu.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.menu.running = False
                pygame.quit()
                sys.exit()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move(-self.player.speed, 0, self.maze)
        if keys[pygame.K_RIGHT]:
            self.player.move(self.player.speed, 0, self.maze)
        if keys[pygame.K_UP]:
            self.player.move(0, -self.player.speed, self.maze)
        if keys[pygame.K_DOWN]:
            self.player.move(0, self.player.speed, self.maze)

        for item in self.maze.items[:]:
            if self.player.rect.colliderect(item.rect):
                self.item_sound.play()
                self.maze.items.remove(item)

        if not self.maze.items:
            self.next_level()

    def draw(self):
        self.screen.fill(WHITE)
        self.maze.draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.flip()
        
    def next_level(self):
        """Avança para o próximo nível ou finaliza o jogo se todos os níveis foram concluídos."""
        if self.current_level < len(LEVELS) - 1:
            self.current_level += 1
            self.show_transition_message(f"Nível {self.current_level + 1}")
            self.maze = Maze(self.current_level)  
            self.player = Player(60, 60)  
        else:
            self.show_victory_message()

    def show_transition_message(self, message):
        """Exibe uma mensagem temporária ao trocar de nível."""
        self.screen.fill(WHITE)
        self.draw_text(message, WIDTH // 2, HEIGHT // 2, BLACK)
        pygame.display.flip()
        pygame.time.delay(2000)  

    def show_victory_message(self):
        self.screen.fill(WHITE)
        self.draw_text("Parabéns! Você venceu!", WIDTH // 2, HEIGHT // 2, BLACK)
        pygame.display.flip()
        pygame.time.delay(3000)
        self.score.save(self.current_level + 1)
        self.menu.running = True
        self.running = False  
        
    def draw_text(self, text, x, y, color):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)
