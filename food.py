import pygame
import random
from music import play_event_sound

class food:
    foods = []
    snake = None
    drawer = None
    width = 0
    heigth = 0

    def __init__(self, snake, drawer):
        self.snake = snake
        self.drawer = drawer
        self.width, self.heigth = self.drawer.get_screen_width_heigth()
        self.add_food()
        self.add_food()


    def add_food(self):
        x = random.randint(0, self.width - 20)
        y = random.randint(0, 600 - 20)
        type = random.randint(0, 4)
        snake_segments = self.snake.snake
        for segment in snake_segments:
            if abs(segment[0] - x) < 20 and abs(segment[1] - y) < 20:
                self.add_food()
                return
        self.foods.append((x, y, type))

    def is_crashed(self, score):
        res_score = score
        for food in self.foods:
            if abs(self.snake.head_x - food[0]) < 20 and abs(self.snake.head_y - food[1]) < 20:
                self.play_sound()
                if food[2] == 0:
                    self.snake.length += 1
                    res_score += 10
                elif food[2] == 4:
                    self.snake.length += 2
                    res_score += 20
                elif food[2] == 1:
                    self.snake.speed *= 1.2
                    res_score *= 1.2
                elif food[2] == 2:
                    self.snake.speed /= 1.2
                    res_score -= 10
                elif food[2] == 3:
                    self.snake.length += 1
                    res_score -= 5
                self.foods.remove(food)
                self.add_food()
        return res_score

    def draw(self):
        self.drawer.draw_food(self.foods)
    
    def play_sound(self):
        play_event_sound()
        