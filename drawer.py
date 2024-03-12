from decorators import try_except_decorator
import pygame
pygame.font.init()
pygame.init()
class drawer:
    
    screen_width = 0
    screen_height = 0
    screen = None
    
    def __init__(self):
        self.read_settings("settings.txt")
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        
    
    @try_except_decorator("Wrong settings file")
    def read_settings(self,file):
        with open(file, "r") as f:
            for line in f:
                if "width" in line:
                    self.screen_width = int(line.split("=")[1].strip())
                elif "height" in line:  
                    self.screen_height = int(line.split("=")[1].strip())
        f.close()
    
    @try_except_decorator("Exception in draw_final_screen")
    def draw_final_screen(self,score):
        self.screen.fill((100, 100, 100))
        big_label = pygame.font.SysFont("arial", 48)
        label = pygame.font.SysFont("arial", 40)
        small_label = pygame.font.SysFont("arial", 16)
        score_label = big_label.render(f"YOUR SCORE: {int(score)}", True, (255, 255, 255))
        finish = label.render("GAME OVER", True, (255, 255, 255))
        quit = small_label.render("Put \"Q\" to exit", True, (255, 255, 255))
        restart = small_label.render("Put \"R\" to restart", True, (255, 255, 255))
        self.screen.blit(quit, (self.screen_width - 380, self.screen_height - 300))
        self.screen.blit(restart, (self.screen_width - 550, self.screen_height - 300))
        self.screen.blit(finish, (self.screen_width - 525, self.screen_height - 350))
        self.screen.blit(score_label, (self.screen_width - 580, self.screen_height - 500))
        pygame.display.update()
        
        
    @try_except_decorator("Exception in refresh_score")    
    def refresh_score(self,num):
        score = pygame.font.SysFont("arial", 18)
        score1 = score.render(f"Score : {num}", True, (255, 0, 0))
        self.screen.blit(score1, (1, 1))
    
    
    @try_except_decorator("Something wrong with live sprite")
    def print_lives(self,lives):
        for i in range(lives):
            heart_surf = pygame.image.load('sprites\\heart.ZoVwa.png')
            head_rect = heart_surf.get_rect(bottomright = (self.screen_width - (i * 36) - 1, 5 + 34))
            self.screen.blit(heart_surf, head_rect)
    
    
    @try_except_decorator("Something wrong with setting sprite")
    def draw_setting(self):
        self.screen.fill((255, 255, 255))
        setting_surf = pygame.image.load("sprites\\setting.png")
        setting_rect = setting_surf.get_rect(bottomright = (self.screen_width - 50, self.screen_height - 100))
        self.screen.blit(setting_surf, setting_rect)
        pygame.display.update()
        
        
    @try_except_decorator("Somtething wrong with head sprite")
    def draw_snake_head(self, x, y, prev_direction):
            head_surf = pygame.image.load('sprites\\head.png')
            head_rect = head_surf.get_rect(bottomright=(x+20,y+20))
            head1_surf = pygame.image.load('sprites\\head1.png')
            head1_rect = head1_surf.get_rect(bottomright=(x+20,y+20))
            if (prev_direction==pygame.K_LEFT):
                flip = pygame.transform.flip(head_surf,True,False)
                self.screen.blit(flip,head_rect)
            elif(prev_direction==pygame.K_RIGHT):
                self.screen.blit(head_surf,head_rect)
            elif(prev_direction==pygame.K_UP):
                self.screen.blit(head1_surf,head1_rect)
            elif(prev_direction==pygame.K_DOWN):
                flip = pygame.transform.flip(head1_surf,False,True)
                self.screen.blit(flip,head1_rect)
    
    
    @try_except_decorator("Something wrong with segment sprite")
    def draw_snake_segment(self,x,y):
        segment_surf = pygame.image.load('sprites\\segment.png')
        segment_rect = segment_surf.get_rect(bottomright=(x+20,y+20))
        self.screen.blit(segment_surf,segment_rect)
        
        
    @try_except_decorator("Something wrong with food sprites")
    def draw_food(self,foods):
        for food in foods:
                if food[2] == 0:
                    food_surf = pygame.image.load('sprites\\c.png')
                elif food[2] == 1:
                    food_surf = pygame.image.load('sprites\\cpp.png')
                elif food[2] == 2:
                    food_surf = pygame.image.load('sprites\\go.png')
                elif food[2] == 3:
                    food_surf = pygame.image.load('sprites\\Ruby.png')
                elif food[2] == 4:
                    food_surf = pygame.image.load('sprites\\sharp.png')
                food_rect = food_surf.get_rect(bottomright=(food[0] + 20, food[1] + 20))
                self.screen.blit(food_surf, food_rect)


    def fill_screen(self):
        self.screen.fill((100, 100, 100))
    
    
    def get_screen_width_heigth(self):
        return self.screen_width,self.screen_height