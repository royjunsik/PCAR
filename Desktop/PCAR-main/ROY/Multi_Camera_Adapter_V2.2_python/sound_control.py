import pygame

def play_mp3(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

#play_mp3('/home/tony8181/Downloads/Please_empty_the_liquid.mp3')