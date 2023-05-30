import pygame
from pathlib import Path
DIR = str(Path(__file__).resolve().parent) #+'/../memory_game'
# print('==== game_done_screen.py 1 ====')
class Page():
    def __init__(self, oil92, oil95, oil98, oilEngine, screw, win) -> None:
        self.background = pygame.image.load(DIR + '/images/background.png').convert_alpha()
        self.background = pygame.transform.scale(self.background, (800, 500))
        self.background.set_alpha(20)

        self.font_32 = pygame.font.Font(DIR + '/fonts/GenSenRounded-M.ttc', 28)
        self.font_50 = pygame.font.Font(DIR + '/fonts/MarkerFelt.ttc', 50)
        self.text_background = pygame.surface.Surface((600, 300))

        self.update_text(oil92, oil95, oil98, oilEngine, screw, win)
        self.text_title_rect = self.text_title.get_rect()
        self.text_title_rect.center = (400, 205)
        self.text_x, self.text_y = 400, 260

    
    def update_text(self, oil92, oil95, oil98, oilEngine, screw, win):
        if win:
            self.text_title = self.font_50.render('Congratulation!  GET', True, (0, 0, 0))
            content = f'獲得92汽油: {oil92},  95汽油: {oil95},  98汽油: {oil98}\n機油: {oilEngine},  螺絲: {screw}'
            # self.text = self.font_32.render(content, True, (255, 255, 255))
            self.text = content
        else:
            self.text_title = self.font_50.render('Game Over', True, (255, 255, 255))
            content = 'sorry, you lose.\n Nothing to get.'
            self.text = self.font_50.render(content, True, (255, 255, 255))
        
    def draw(self):
        screen.blit(self.background, (0, 0))
        screen.blit(self.text_title, self.text_title_rect)
        for i, line in enumerate(self.text.split('\n')):
            text = self.font_32.render(line, True, (255, 255, 255))
            text_rect = text.get_rect()
            text_rect.center = (self.text_x, self.text_y + i * 40)
            screen.blit(text, text_rect)
      
def main(oil92=12, oil95=12, oil98=4, oilEngine=3, screw=23, win=True):
    pygame.init()
    # print('==== game_done_screen.py 3 ====')
    FPS = 60
    clock = pygame.time.Clock()
    global screen
    screen = pygame.display.set_mode((800, 500))
    # print('==== game_done screen start ====')
    pygame.display.set_caption('Game Done')
    page = Page(oil92, oil95, oil98, oilEngine, screw, win)
    running = True
    while running:
        page.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()

if __name__ == '__main__':
    pass
    # print('==== game_done_screen.py 2 ====')
    # screen = pygame.display.set_mode((800, 500))
    # main()
