import pygame, os
pygame.init()
# init pygame before importing other dependencies

from screens.main_screen import MainScreen

def main():
    main_screen = MainScreen()
    main_screen.run()   

if __name__ == "__main__":
    main()
