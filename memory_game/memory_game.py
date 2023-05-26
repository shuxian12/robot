import pygame, cv2, random, os, time
from pathlib import Path
DIR = str(Path(__file__).resolve().parent)#+'/../memory_game'

pygame.init()

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 860
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Memory Game')

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

FPS = 60
clock = pygame.time.Clock()


class Tile(pygame.sprite.Sprite):
    def __init__(self, filename, x, y):
        super().__init__()

        self.name = filename.split('.')[0]
        self.original_image = pygame.image.load(DIR+'/images/hololive/vtuber/' + filename)
        self.back_image = pygame.image.load(DIR+'/images/hololive/background.png')

        self.image = self.back_image
        self.rect = self.image.get_rect(topleft = (x, y))
        self.shown = False

    def update(self):
        self.image = self.original_image if self.shown else self.back_image

    def show(self):
        self.shown = True
    def hide(self):
        self.shown = False

class Game():
    def __init__(self):
        self.level = 1
        self.level_complete = False
        self.game_over = False
        self.you_win = False

        # vtubers
        self.all_vtubers = [f for f in os.listdir(DIR+'/images/hololive/vtuber') if os.path.join(DIR+'/images/hololive/vtuber', f) if f.endswith('.png')]
        self.img_width, self.img_height = (126, 176)
        self.padding = 20
        self.margin_top = 190
        self.cols = 4
        self.rows = 2
        self.width = 1280

        self.tiles_group = pygame.sprite.Group()

        # flipping & timing
        self.flipped = []
        self.frame_count = 0
        self.block_game = False

        # generate first level
        self.generate_level()

        # initialize video
        self.is_video_playing = True
        self.play = pygame.image.load(DIR+'/images/play.png').convert_alpha()
        self.stop = pygame.image.load(DIR+'/images/stop.png').convert_alpha()
        self.video_toggle = self.play
        self.video_toggle_rect = self.video_toggle.get_rect(topright = (WINDOW_WIDTH - 50, 10))
        self.get_video()

        # initialize music
        self.is_music_playing = True
        self.sound_on = pygame.image.load(DIR+'/images/speaker.png').convert_alpha()
        self.sound_off = pygame.image.load(DIR+'/images/mute.png').convert_alpha()
        self.music_toggle = self.sound_on
        self.music_toggle_rect = self.music_toggle.get_rect(topright = (WINDOW_WIDTH - 10, 10))

        # load music
        pygame.mixer.music.load(DIR+'/sounds/アイドル.mp3')
        pygame.mixer.music.set_volume(.3)
        pygame.mixer.music.play()

        # initialize timer
        self.time_limit = 5.0
        self.timer = pygame.time.get_ticks()
        self.timer_font = pygame.font.Font(DIR+'/fonts/Comic Sans MS Bold.ttf', 24)
        self.timer_text = self.timer_font.render('Time: {:04.1f}'.format(self.time_limit), True, WHITE)
        self.timer_rect = self.timer_text.get_rect(topright = (WINDOW_WIDTH - 100, 10))

        # initialize game win image
        self.game_win_img = pygame.image.load(DIR+'/images/game_win.gif').convert_alpha()
        self.game_win_rect = self.game_win_img.get_rect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

    def update(self, event_list):
        if self.is_video_playing:
            self.success, self.img = self.cap.read()

        self.user_input(event_list)
        self.draw()
        self.check_level_complete(event_list)
    
    def update_timer(self):
        self.time_limit -= 0.1
        if self.time_limit >= 0:
            self.timer_text = self.timer_font.render('Time: {:04.1f}'.format(self.time_limit), True, WHITE)
        if self.time_limit <= 0:
            self.game_over = True

    def game_is_over(self):
        # over_font = pygame.font.Font('fonts/Little Alien.ttf', 72)
        # self.game_over_text = over_font.render('Game Over', True, WHITE)
        self.game_over_img = pygame.image.load(DIR+'/images/game_over.jpg').convert_alpha()
        self.game_over_rect = self.game_over_img.get_rect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
        screen.blit(self.game_over_img, self.game_over_rect)


    def check_level_complete(self, event_list):
        if not self.block_game:
            for event in event_list:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # check two cards are same
                    for tile in self.tiles_group:
                        if tile.rect.collidepoint(event.pos):
                            self.flipped.append(tile.name)
                            tile.show()
                            if len(self.flipped) == 2:
                                if self.flipped[0] != self.flipped[1]:
                                    self.block_game = True
                                else:
                                    self.flipped = []
                                    for tile in self.tiles_group:
                                        if tile.shown:
                                            self.level_complete = True
                                        else:
                                            self.level_complete = False
                                            break
        else:
            self.frame_count += 1
            if self.frame_count == FPS:
                self.frame_count = 0
                self.block_game = False

                for tile in self.tiles_group:
                    if tile.name in self.flipped:
                        tile.hide()
                self.flipped = []


    def generate_level(self):
        self.vtubers = self.select_random_vtubers()
        self.level_complete = False
        self.rows = 3
        self.cols = 8
        self.generate_tileset(self.vtubers)

    def generate_tileset(self, vtubers):
        self.cols = self.rows = self.cols if self.cols >= self.rows else self.rows

        TILES_WIDTH = (self.img_width * self.cols + self.padding * 3)
        LEFT_MARING = RIGHT_MARGIN = (self.width - TILES_WIDTH) // 3
        #tiles = []
        self.tiles_group.empty()

        for i in range(len(vtubers)):
            x = LEFT_MARING + ((self.img_width + self.padding) * (i % self.cols))   # position of card
            y = self.margin_top + (i // self.rows * (self.img_height + self.padding))
            tile = Tile(vtubers[i], x, y)
            self.tiles_group.add(tile)

    def select_random_vtubers(self):
        vtubers = random.sample(self.all_vtubers, 12)
        vtubers_copy = vtubers.copy()
        vtubers.extend(vtubers_copy)
        random.shuffle(vtubers)
        return vtubers

    def user_input(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:      # event.button == 1 means left click
                if self.music_toggle_rect.collidepoint(pygame.mouse.get_pos()): # music sound toggle control
                    if self.is_music_playing:
                        self.is_music_playing = False
                        self.music_toggle = self.sound_off
                        pygame.mixer.music.pause()
                    else:
                        self.is_music_playing = True
                        self.music_toggle = self.sound_on
                        pygame.mixer.music.unpause()
                if self.video_toggle_rect.collidepoint(pygame.mouse.get_pos()): # anime control 
                    if self.is_video_playing:
                        self.is_video_playing = False
                        self.video_toggle = self.stop
                    else:
                        self.is_video_playing = True
                        self.video_toggle = self.play

    def draw(self):
        screen.fill(BLACK)

        # fonts
        title_font = pygame.font.Font(DIR+'/fonts/Little Alien.ttf', 44)
        content_font = pygame.font.Font(DIR+'/fonts/Little Alien.ttf', 24)

        # text
        title_text = title_font.render('Memory Game', True, WHITE)
        title_rect = title_text.get_rect(midtop = (WINDOW_WIDTH // 2, 10))

        info_text = content_font.render('Find 2 of each', True, WHITE)
        info_rect = info_text.get_rect(midtop = (WINDOW_WIDTH // 2, 80))

        if self.is_video_playing:
            if self.success:
                screen.blit(pygame.image.frombuffer(self.img.tobytes(), self.shape, 'BGR'), (0, 120))
            else:
                self.get_video()
        else:
            screen.blit(pygame.image.frombuffer(self.img.tobytes(), self.shape, 'BGR'), (0, 120))

        screen.blit(title_text, title_rect)
        screen.blit(info_text, info_rect)
        pygame.draw.rect(screen, WHITE, (WINDOW_WIDTH - 90, 0, 100, 50))
        screen.blit(self.video_toggle, self.video_toggle_rect)
        screen.blit(self.music_toggle, self.music_toggle_rect)
        screen.blit(self.timer_text, self.timer_rect)

        # draw tileset
        self.tiles_group.draw(screen)
        self.tiles_group.update()

        if self.level_complete:
            self.you_win = True

    def get_video(self):
        self.cap = cv2.VideoCapture(DIR+'/video/background.mp4')
        self.success, self.img = self.cap.read()
        self.shape = self.img.shape[1::-1]

def main(return_dict={'you_win': False}):
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Memory Game')
    game = Game()
    pygame.time.set_timer(pygame.USEREVENT, millis=100)
    running = True
    while running:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.USEREVENT:
                game.update_timer()

        game.update(event_list)
        pygame.display.update()

        if game.game_over:
            game.game_is_over()
            pygame.display.update()
            time.sleep(1)
            running = False

        if game.you_win:
            screen.blit(game.game_win_img, game.game_win_rect)
            pygame.display.update()
            time.sleep(1)
            running = True
            break

        clock.tick(FPS)

    pygame.quit()
    print(running if running else 'Game Over')
    if not return_dict: return_dict['running'] = True#running
    return running

if __name__ == '__main__':
    main()
    # print("{:02.1f}".format(60))
    # print("{:04.1f}".format(6))
    # game = Game()
    # def event():
    #     pygame.USEREVENT = pygame.USEREVENT-1
    #     timer_font = pygame.font.Font('fonts/Little Alien.ttf', 24)
    #     timer_text = timer_font.render('Time: {:02d}'.format(pygame.USEREVENT), True, WHITE)
    #     timer_rect = timer_text.get_rect(topright = (WINDOW_WIDTH - 90, 10))
    # USEREVENT = pygame.USEREVENT-1
    # pygame.time.set_timer(USEREVENT, millis=1000)
    # while(True):
    #     if pygame.event.get(USEREVENT):
    #         pygame.USEREVENT -= 1000
    #         print(pygame.USEREVENT)
    #     if pygame.USEREVENT == 0:
    #         break

