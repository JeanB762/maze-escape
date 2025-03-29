import pygame
from src.Config import WIDTH, HEIGHT, WHITE, FPS, BLACK, MAZE_LAYOUT_1, MAZE_LAYOUT_2, MAZE_LAYOUT_3, MAZE_LAYOUT_4, MAZE_LAYOUT_5
from src.Player import Player
from src.Maze import Maze

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Maze Escape")
        self.clock = pygame.time.Clock()
        self.running = True

        # Lista de layouts dos níveis
        self.levels = [MAZE_LAYOUT_1, MAZE_LAYOUT_2, MAZE_LAYOUT_3, MAZE_LAYOUT_4, MAZE_LAYOUT_5]
        self.current_level = 0

        self.load_level()

        pygame.mixer.init()
        pygame.mixer.music.load("assets/background_music.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        self.item_sound = pygame.mixer.Sound("assets/achievement.mp3")
        self.font = pygame.font.Font(None, 40)

    def load_level(self):
        """Carrega o nível atual."""
        self.maze = Maze(self.levels[self.current_level])
        self.player = Player(60, 60)

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

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

        # Verifica se o jogador pegou um item
        for item in self.maze.items[:]:
            if self.player.rect.colliderect(item.rect):
                self.item_sound.play()
                self.maze.items.remove(item)

        # Se todos os itens forem coletados, avançar para o próximo nível
        if not self.maze.items:
            self.next_level()

    def draw(self):
        self.screen.fill(WHITE)
        self.maze.draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.flip()

    def next_level(self):
        """Avança para o próximo nível ou finaliza o jogo se todos os níveis foram concluídos."""
        if self.current_level < len(self.levels) - 1:
            self.current_level += 1
            self.show_transition_message(f"Nível {self.current_level + 1}")
            self.load_level()
        else:
            self.show_victory_message()

    def show_transition_message(self, message):
        """Exibe uma mensagem temporária ao trocar de nível."""
        self.screen.fill(WHITE)
        self.draw_text(message, WIDTH // 2, HEIGHT // 2, BLACK)
        pygame.display.flip()
        pygame.time.delay(2000)  # Espera 2 segundos antes de carregar o próximo nível

    def show_victory_message(self):
        self.screen.fill(WHITE)
        self.draw_text("Parabéns! Você venceu!", WIDTH // 2, HEIGHT // 2, BLACK)
        pygame.display.flip()
        pygame.time.delay(3000)
        self.running = False

    def draw_text(self, text, x, y, color):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)
