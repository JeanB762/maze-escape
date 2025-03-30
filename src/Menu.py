import sys
import pygame
from src.Config import WIDTH, HEIGHT, MENU_OPTION, WHITE, CYAN
from src.Score import Score

class Menu:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        self.font = pygame.font.Font(None, 40)
        self.running = True
        
        self.surf = pygame.image.load('./assets/MenuBg.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (WIDTH, HEIGHT))
        self.rect = self.surf.get_rect(left=0, top=0)

        self.logo = pygame.image.load('./assets/logo.png').convert_alpha()
        self.logo = pygame.transform.scale(self.logo, (200, 200))
        self.logo_rect = self.logo.get_rect(center=(WIDTH // 2, HEIGHT // 4))

        self.menu_items = MENU_OPTION
        self.selected_item = 0  
        
        self.score = Score(self.screen)
        
    def draw_text(self, text, x, y, color):
        """Desenha o texto na tela."""
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)

    def draw(self):
        """Desenha o menu na tela."""
        self.screen.blit(source=self.surf, dest=self.rect)
        self.screen.blit(self.logo, self.logo_rect)

        for i, item in enumerate(self.menu_items):            
            color = WHITE if i != self.selected_item else CYAN  
            self.draw_text(item, WIDTH // 2, HEIGHT // 2 + i * 50, color)

        pygame.display.flip()

    def handle_events(self):
        """Lida com os eventos de teclado e seleciona as opções do menu."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.game.running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:  
                    self.selected_item = (self.selected_item + 1) % len(self.menu_items)
                elif event.key == pygame.K_UP:  
                    self.selected_item = (self.selected_item - 1) % len(self.menu_items)
                elif event.key == pygame.K_RETURN:  
                    self.select_option()

    def select_option(self):
        if self.selected_item == 0:
            self.game.running = True
            self.game.menu.running = False
            self.game.start_new_game()
        elif self.selected_item == 1:
            self.score.show()
        elif self.selected_item == 2:
            self.running = False
            self.game.running = False
            pygame.quit()
            sys.exit()
