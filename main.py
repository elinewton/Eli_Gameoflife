import sys,pygame
from view import GoLView
from model import GoLModel
from controller import GoLController

def rungame():
    pygame.init()
    clock = pygame.time.Clock()
    view = GoLView()
    model = GoLModel(view.width,view.height)
    ctrl = GoLController(view,model)
    view.setModel(model)


    while True:
        clock.tick(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
                #ctrl.eventDispatch(event)
        
        model.updateGrid()
        view.update()
        

if __name__ == '__main__':
    rungame()