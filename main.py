import pygame, sys, os, random, json, math
import utils

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((500, 300))
        self.display = pygame.Surface((self.screen.get_size()[0]/4, self.screen.get_size()[1]/4))

        self.clock = pygame.time.Clock()

        with open('list.json', 'r') as file:
            self.data = json.load(file)


        self.Center = (self.display.get_width()/2, self.display.get_height()/2)
        self.font = utils.Font('medium-font.png', (255,255,255))

        self.number = random.randint(0, len(self.data['names']) - 1)
        self.picked = self.data['names'][self.number]

        self.select_sound = pygame.mixer.Sound('select.wav')

        self.visurf = pygame.Surface((self.display.get_width(), self.display.get_height()))
        self.line_width = 5
        self.lines = 15

    def run(self):
        while True:
            self.visurf.fill((0,0,40))
            for i in range(0,self.lines):
                pygame.draw.line(self.visurf, (0,0,20), (i * self.visurf.get_width()/self.lines + self.line_width/2, 0), (i * self.visurf.get_width()/self.lines + self.line_width/2, self.visurf.get_height()), self.line_width)

            self.display.blit(self.visurf, (0,0))

            self.font.render(self.display, self.picked, (self.Center[0] - self.font.get_text_width(self.picked)/2, self.Center[1] - 2))

            self.font.render(self.display, str(self.number + 1)+'/'+str(len(self.data['names'])), (1, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.number = min(len(self.data['names']) - 1, self.number + 1)
                        self.picked = self.data['names'][self.number]
                        self.select_sound.play()
                    if event.key == pygame.K_LEFT:
                        self.number = max(0, self.number - 1)
                        self.picked = self.data['names'][self.number]
                        self.select_sound.play()

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.flip()
            self.clock.tick(60)

Game().run()
