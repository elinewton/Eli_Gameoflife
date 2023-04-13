import sys,pygame
from view import GoLView
from model import GoLModel
from controller import GoLController
from pygame import mixer
mixer.init()
mixer.music.load('GoL Music.mp3')
mixer.music.play()
pygame.mixer.find_channel()
bidenSound = pygame.mixer.Sound('Joe Biden GoL.mp3')
pygame.mixer.Sound.play(bidenSound)


def rungame():
    pygame.init()
    clock = pygame.time.Clock()
    view = GoLView()
    model = GoLModel(view.width,view.height)
    ctrl = GoLController(model,view)
    view.setModel(model)


    while True:
        clock.tick(8)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            else:
                ctrl.eventDispatch(event)
        
        if ctrl.go:
            model.updateGrid()
        view.update()
        

if __name__ == '__main__':
    rungame()