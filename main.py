import sys,pygame
from view import GoLView

def rungame():
    pygame.init()
    view = GoLView()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        view.update()
        


if __name__ == '__main__':
    rungame()