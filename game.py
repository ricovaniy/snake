import snake as sn
import time
from music import play_background
import pickle
from collections import deque
import os
import food as foo
import drawer as dr
try:
    import pygame
except:
    import pip
    pip.main(["install", "--quiet", "pygame"])
    import pygame
    
class game:
    def __init__(self):
        pygame.font.init()
        pygame.init()
        play_background()


    def start(self,drawer):
        global score
        try:
            with open('save_file.pickle', 'rb') as f:
                game_state = pickle.load(f)
            lives = game_state['lives']
            snake_data = game_state["snake"]
            food_data = game_state['food']
            score = game_state['score']
            os.remove("save_file.pickle")
        except:
            lives = 3
            snake_data = {'x': 20, 'y':20, 'length':1, 'direction': pygame.K_RIGHT, 'snake': deque(), 'speed': 10, 'prev_dir':None} 
            food_data = []
            score = 0
            
        snake = sn.Snake(snake_data['x'], snake_data['y'], drawer)
        snake.length = snake_data['length']
        snake.direction = snake_data['direction']
        snake.snake = snake_data['snake']
        snake.speed = snake_data['speed']
        snake.prev_direction = snake_data['prev_dir']
        food = foo.food(snake, drawer)
        if len(food_data)>0:
            food.foods.clear()
            food.foods = food_data
        pygame.display.set_caption("Snake")
        running = True
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_state = {"lives": lives, "snake": {'x': snake.head_x, 
                                                            'y': snake.head_y,
                                                            'length':snake.length,
                                                            'direction': snake.direction,
                                                            'snake': snake.snake,
                                                            'speed': snake.speed, 
                                                            'prev_dir': snake.prev_direction} , "food": food.foods, "score": score}
                    with open('save_file.pickle', 'wb') as f:
                        pickle.dump(game_state, f)
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                        pause = False
                        snake.direction = event.key
                    elif event.key == pygame.K_ESCAPE:
                        pause = True
                        drawer.draw_setting()
                    else:
                        pause = False
            if not running: break
            if pause: continue
            if lives == 0:
                food.foods.clear()
                running = False
                snake.snake.clear()
            snake.move()

            crash = snake.check_crash()
            score = food.is_crashed(score)

            if crash:
                lives -= 1
                snake.head_x = 50
                snake.head_y = 50
                snake.direction = pygame.K_RIGHT
                snake.prev_direction = None
                snake.snake.clear()
            if running:
                drawer.fill_screen()
                food.draw()
                snake.draw_snake()
                drawer.refresh_score(int(score))
                drawer.print_lives(lives)
                pygame.display.update()
                time.sleep(snake.speed / 100)
            else:
                drawer.draw_final_screen(int(score))


    def run(self):
        drawer = dr.drawer()
        self.start(drawer)
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        exit()
                    elif event.key == pygame.K_r:
                        self.start(drawer)
                else:
                    drawer.draw_final_screen(int(score))

