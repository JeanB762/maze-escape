WIDTH, HEIGHT = 960, 720
TILE_SIZE = 60
ACHIEVEMENT_SIZE = 35
PLAYER_SIZE_WIDTH = 37
PLAYER_SIZE_HEIGHT = 50
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

MENU_OPTION = ["Novo Jogo", "Ver Pontuação", "Sair"]

SCORE_POS = {'Title': (WIDTH / 2, 50),
             'EnterName': (WIDTH / 2, 80),
             'Label': (WIDTH / 2, 90),
             'Name': (WIDTH / 2, 110),
             0: (WIDTH / 2, 110),
             1: (WIDTH / 2, 130),
             2: (WIDTH / 2, 150),
             3: (WIDTH / 2, 170),
             4: (WIDTH / 2, 190),
             5: (WIDTH / 2, 210),
             6: (WIDTH / 2, 230),
             7: (WIDTH / 2, 250),
             8: (WIDTH / 2, 270),
             9: (WIDTH / 2, 290),
             }

#16 largura por 12 de altura
# Layouts de teste
MAZE_LAYOUT_1_TEST = [
    "1111111111111101",
    "1000200000010001",
    "1011111111011101",
    "1010000001000001",
    "1010111101011101",
    "1010100101011001",
    "1010110101010011",
    "1010010101011011",
    "1011110101011001",
    "1000000101000001",
    "1111110100011101",
    "1111111111111111"
]

MAZE_LAYOUT_2_TEST = [
    "1111111111111111",
    "1002000000000101",
    "1011111111111101",
    "1010000000000101",
    "1010111011100101",
    "1010101000100101",
    "1010101110100101",
    "1000101010100001",
    "1110101010111111",
    "1000100000000001",
    "1011111111111101",
    "1111111111111111"
]


MAZE_LAYOUT_1 = [
    "1111111111111101",
    "1000000002012001",
    "1011111111011101",
    "1010000001000001",
    "1010111101011101",
    "1010100101011021",
    "1010110101010011",
    "1010210101011011",
    "1011110101011001",
    "1000000101000001",
    "1111110100011101",
    "1111111111111111"
]

MAZE_LAYOUT_2 = [
    "1111111111111111",
    "1000000000000121",
    "1011111111111101",
    "1010000000000101",
    "1010111011100101",
    "1010101000100101",
    "1010101110100101",
    "1000101210100001",
    "1110101010111111",
    "1000100000020001",
    "1211111111111101",
    "1111111111111111"
]

MAZE_LAYOUT_3 = [
    "1111111111111111",
    "1000001000020001",
    "1011111110111101",
    "1010000100000101",
    "1010112101110101",
    "1010010101200101",
    "1011010101110101",
    "1010010001000101",
    "1010010101011101",
    "1010101111011101",
    "1000000012011201",
    "1111111111111111"
]

MAZE_LAYOUT_4 = [
    "1111111111111111",
    "1000000001000021",
    "1011111101111101",
    "1010020100000001",
    "1010110110110101",
    "1010000000000101",
    "1010111111100101",
    "1010120000100101",
    "1010111110111111",
    "1010000000000201",
    "1011111111111101",
    "1111111111111111"
]

MAZE_LAYOUT_5 = [
    "1111111111111111",
    "1000000020000001",
    "1011111111111101",
    "1012100000122101",
    "1010101110122101",
    "1010101000102101",
    "1010101011100101",
    "1010101000000101",
    "1010101111111101",
    "1010001120000001",
    "1000111111111111",
    "1111111111111111"
]

LEVELS = [MAZE_LAYOUT_1_TEST, MAZE_LAYOUT_2_TEST] #test
# LEVELS = [MAZE_LAYOUT_1, MAZE_LAYOUT_2, MAZE_LAYOUT_3, MAZE_LAYOUT_4, MAZE_LAYOUT_5]