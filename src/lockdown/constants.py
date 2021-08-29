APP_NAME = 'lockdown'
APP_VERSION = 0.1

# screen / animation values
WINDOW_SIZE = (1000, 778)
FPS = 400
ANTI_FRICTION = 2
GAME_SCREEN_START = (30,30)
GAME_SCREEN_END = (805,748)

# level
MAX_LEVEL = 1
LEVEL_COMPLETE = 1
GAME_COMPLETE = 2

# colors
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255,0,0)
GREEN = (0,204,34)
Y_GREEN = (154, 205,50)
GRAY = (222, 222, 222)

# virus data
VIRUS_POINTS = [10, 50, 30, 40]
VIRUS_HIT_LIFE = [1, 1, 5, 6]
VIRUS_IMAGE =['covid_a1.png','covid_b1.png','covid_c1.png','covid_d1.png']

# brick data
BRICK_IMAGE =['brick1_normal.png','brick_life.png','brick_speed.png','brick_slow.png']

# sound

BG_MUSIC = 'bg_sound.flac'
INTRO_MUSIC = 'intro.flac'
WALL_BOUNCE = 'bounce.wav'
BRICK_BOUNCE = 'metal_hit.wav'
VIRUS_KILL = 'virus_kill.wav'
VIRUS_BOUNCE = 'virus_bounce.wav'
WARNING_MUSIC = 'warning.wav'

# fonts and images

FONT_MAIN_1 = 'minecraft.otf'
FONT_SUB_1 = "calibri"
COVID_TIPS = "covid_tips.gif"

# string resources

TEXT_GAME_TITLE = 'Lockdown'
TEXT_OPENING_SCREEN_INTS1 = 'Press the SPACEBAR to start the game'
TEXT_START = 'Start'
TEXT_GAMEOVER = 'Game Over'
TEXT_SCORE = 'Score'
TEXT_HIGH_SCORE = 'High Score'
TEXT_LEVEL_START = 'Press the SPACEBAR to begin'
TEXT_LIFE = 'Life'
TEXT_LEVEL = 'Level'
TEXT_ENTER_RESTART = 'Press [ENTER] to Restart the game'
TEXT_ESC_QUIT = 'Press [ESC] to Quit the game'
TEXT_FUTURE = 'Game is under development, more to come!'
TEXT_LEVEL_COMPLETE = 'Level Complete'
TEXT_GAME_COMPLETE = 'Game Complete'
TEXT_ENTER_NEXT = 'Press [ENTER] to move to the next level'
TEXT_STATS_DISPLAY = 'GAME STATS'
TEXT_END_FAILEDMESSAGE = 'You have failed the city!'
TEXT_GAME_COMPLETED = "GAME COMPLETE"
TEXT_END_SUCEEDMESSAGE = 'You saved the city!'
