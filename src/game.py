import pygame
from src.config import WIDTH, HEIGHT, WHITE, FPS, BLACK
from src.player import Player
from src.maze import Maze

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Jogo do Labirinto")
        self.clock = pygame.time.Clock()
        self.running = True

        self.maze = Maze()
        self.player = Player(40, 40)

        # 🎵 Música de fundo
        pygame.mixer.init()
        pygame.mixer.music.load("assets/background_music.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        # 📝 Fonte para a mensagem de vitória
        self.font = pygame.font.Font(None, 40)  # Fonte padrão, tamanho 40

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
        self.maze.items = [item for item in self.maze.items if not self.player.rect.colliderect(item.rect)]

        # Se todos os itens forem coletados, mostrar mensagem na tela
        if not self.maze.items:
            self.show_victory_message()

    def draw(self):
        self.screen.fill(WHITE)
        self.maze.draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.flip()

    def show_victory_message(self):
        self.screen.fill(WHITE)  # Limpa a tela
        self.draw_text("Parabéns! Você venceu!", WIDTH // 2, HEIGHT // 2, BLACK)
        pygame.display.flip()
        pygame.time.delay(3000)  # Mantém a mensagem na tela por 3 segundos
        self.running = False  # Encerra o jogo

    def draw_text(self, text, x, y, color):
        """ Desenha um texto na tela """
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)
