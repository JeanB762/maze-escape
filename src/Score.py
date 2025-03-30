import sys
import pygame
from pygame.font import Font
from datetime import datetime
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE

from src.DBProxy import DBProxy
from src.Config import SCORE_POS, WIDTH, HEIGHT, WHITE, CYAN

class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./assets/MenuBg.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (WIDTH, HEIGHT))
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def save(self, level):
        db_proxy = DBProxy('game_scores.db')
        name = ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'YOU WIN!!', CYAN, SCORE_POS['Title'])
            text = 'Enter Player Name (4 characters):'
            self.score_text(20, text, WHITE, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'level': level, 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode
            self.score_text(20, name, WHITE, SCORE_POS['Name'])
            pygame.display.flip()
            pass

    def show(self):
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(48, 'TOP 10 SCORE', CYAN, SCORE_POS['Title'])
        self.score_text(20, 'NAME     LEVEL           DATE      ', CYAN, SCORE_POS['Label'])
        db_proxy = DBProxy('game_scores.db')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            name, level, date = player_score
            self.score_text(20, f'{name}     {level:05d}     {date}', CYAN,
                            SCORE_POS[list_score.index(player_score)])
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"
