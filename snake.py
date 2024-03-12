import pygame
from collections import deque
class Snake:
    
    head_x = 0
    head_y = 0
    snake = deque()
    prev_direction = None
    direction = pygame.K_RIGHT
    drawer = None
    length = 1
    screen = None
    speed=10
    
    
    def __init__(self, x, y, drawer):
        self.head_x = x
        self.head_y = y
        self.snake.append((x,y))
        self.drawer = drawer
        self.screen = drawer.screen
    
    def move(self):
        if self.direction==pygame.K_RIGHT:
            if (self.length!=1 and self.prev_direction==pygame.K_LEFT):
                self.head_x-=20
            else:
                self.head_x+=20
                self.prev_direction=self.direction
        elif self.direction==pygame.K_LEFT:
            if (self.length!=1 and self.prev_direction==pygame.K_RIGHT):
                self.head_x+=20
            else:
                self.head_x-=20
                self.prev_direction=self.direction
        elif self.direction==pygame.K_DOWN:
            if (self.length!=1 and self.prev_direction==pygame.K_UP):
                self.head_y-=20
            else:
                self.head_y+=20
                self.prev_direction=self.direction
        elif self.direction==pygame.K_UP:
            if (self.length!=1 and self.prev_direction==pygame.K_DOWN):
                self.head_y+=20
            else:
                self.head_y-=20
                self.prev_direction=self.direction
    
    
    def draw_snake(self):
        self.snake.append((self.head_x,self.head_y))
        if (len(self.snake)>self.length):
            self.snake.popleft()
        for i in range(len(self.snake)-1,-1,-1):
            segment = self.snake[i]
            if (i==len(self.snake)-1):        
                self.drawer.draw_snake_head(segment[0], segment[1], self.prev_direction)
            else:
                self.drawer.draw_snake_segment(segment[0],segment[1])
                
           
            
            
    def check_crash(self):
        width = self.screen.get_size()[0]
        height = self.screen.get_size()[1]
        if (self.head_x not in range(0,width) or self.head_y not in range(0,height)):
            return True
        for segment in self.snake:
            if abs(self.head_x-segment[0])<20 and abs(self.head_y-segment[1])<20:
                return True
        else: 
            return False
            
    
        
    
    