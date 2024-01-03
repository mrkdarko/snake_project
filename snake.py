import random
import pygame
import time

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
background = (80, 120, 150)
blue = (0, 0, 200)
green = (0, 200, 0)
red = (200, 0, 0)
snake_unit = 10
dis_x = 640
dis_y = 480
speed = 10
game_font = pygame.font.SysFont("comicsansms", 25)
score_font = pygame.font.SysFont("comicsansms", 30)
clock = pygame.time.Clock()

dis = pygame.display.set_mode((dis_x, dis_y))
pygame.display.set_caption('Snake by Kwabena')


def info(inf, color):
    message = game_font.render(inf, True, color)
    dis.blit(message, [dis_x / 5, dis_y / 2])


def points(point):
    point = score_font.render("Points: " + str(point), True, red)
    dis.blit(point, [0, 0])


def snake_func(snake_size, li_snake):
    for cordinate in li_snake:
        pygame.draw.rect(dis, blue, [cordinate[0], cordinate[1], snake_size, snake_size])


def gameloop():
    end = False
    game_close = False

    position_x = random.randint(0, 640)
    position_y = random.randint(0, 480)
    x_change = 0
    y_change = 0
    x_food = int(random.random() * 640)  # Adjusted to the game window dimensions
    y_food = random.randint(10, 470)
    snake_list = []
    snake_length = 1

    current_direction = ""  # Initial direction

    while not end:
        while game_close == True:
            dis.fill(background)
            info("you lost! (Q)uit or (R)eplay", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = True
                    game_close = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        end = True
                        game_close = False
                    if event.key == pygame.K_r:
                        gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and current_direction != "RIGHT":
                    x_change = -snake_unit
                    y_change = 0
                    current_direction = "LEFT"
                elif event.key == pygame.K_RIGHT and current_direction != "LEFT":
                    x_change = snake_unit
                    y_change = 0
                    current_direction = "RIGHT"
                elif event.key == pygame.K_UP and current_direction != "DOWN":
                    x_change = 0
                    y_change = -snake_unit
                    current_direction = "UP"
                elif event.key == pygame.K_DOWN and current_direction != "UP":
                    x_change = 0
                    y_change = snake_unit
                    current_direction = "DOWN"

        if position_x >= dis_x or position_x <= 0 or position_y >= dis_y or position_y < 0:
            game_close = True

        position_x += x_change
        position_y += y_change
        dis.fill(background)
        pygame.draw.rect(dis, black, [0, 0, dis_x, dis_y], 6)

        pygame.draw.rect(dis, green, [x_food, y_food, snake_unit, snake_unit])
        snake_head = []
        snake_head.extend([position_x, position_y])
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            snake_list.pop(0)

        for unit in snake_list[:-1]:
            if unit == snake_head:
                game_close = True

        snake_func(snake_unit, snake_list)
        points(snake_length - 1)
        pygame.display.update()

        if (
                position_x < x_food + snake_unit
                and position_x + snake_unit > x_food
                and position_y < y_food + snake_unit
                and position_y + snake_unit > y_food
        ):
            x_food = int(random.random() * 640)
            y_food = random.randint(10, 470)
            snake_length += 1

        clock.tick(speed)

    pygame.quit()
    quit()


gameloop()
