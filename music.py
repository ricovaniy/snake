from decorators import try_except_decorator
import pygame

@try_except_decorator("something wrong with background.mp3")
def play_background():
    pygame.mixer.music.load("background.mp3")
    pygame.mixer.music.play(-1)
    
    
@try_except_decorator("Something wrong with event.mp3")
def play_event_sound():
        eat_sound = pygame.mixer.Sound("event.mp3")
        eat_sound.set_volume(0.3)
        eat_sound.play()