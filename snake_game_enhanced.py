import pygame
import time
import random
import os

pygame.init()
pygame.mixer.init()

# Set up display
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("🐍 Enhanced Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)
gray = (50, 50, 50)

# Sounds
try:
    pygame.mixer.music.load("background.mp3")
    eat_sound = pygame.mixer.Sound("eat.wav")
    gameover_sound = pygame.mixer.Sound("gameover.wav")
    pygame.mixer.music.play(-1)
except:
    print("Sound files not found. Proceeding without sound.")

# Snake settings
block = 10
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 20)

def draw_text(msg, color, y_offset=0):
    text = font.render(msg, True, color)
    rect = text.get_rect(center=(width // 2, height // 2 + y_offset))
    screen.blit(text, rect)

def draw_snake(block, snake_list):
    for i, pos in enumerate(snake_list):
        color = green if i == len(snake_list) - 1 else gray
        pygame.draw.rect(screen, color, [pos[0], pos[1], block, block])

def show_score(score, high_score):
    value = score_font.render(f"Score: {score}  High Score: {high_score}", True, white)
    screen.blit(value, [10, 10])

def get_high_score():
    try:
        with open("highscore.txt", "r") as f:
            scores = [int(line.strip()) for line in f if line.strip().isdigit()]
            return max(scores) if scores else 0
    except:
        return 0

def save_high_score(score):
    with open("highscore.txt", "a") as f:
        f.write(str(score) + "\n")

def start_menu():
    screen.fill(black)
    draw_text("🐍 Welcome to Snake Game", white, -40)
    draw_text("Press SPACE to Start", green, 0)
    draw_text("Press Q to Quit", red, 40)
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
                if event.key == pygame.K_q:
                    pygame.quit(); quit()

def pause_game():
    paused = True
    draw_text("Paused - Press P to Resume", white)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                paused = False

def game_loop():
    x, y = width // 2, height // 2
    dx, dy = block, 0  # default movement right
    length = 3
    snake = [[x - block * i, y] for i in range(length)]
    speed = 15
    high_score = get_high_score()

    foodx = round(random.randrange(0, width - block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - block) / 10.0) * 10.0

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -block, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = block, 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -block
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, block
                elif event.key == pygame.K_p:
                    pause_game()

        x += dx
        y += dy

        if x >= width or x < 0 or y >= height or y < 0:
            if 'gameover_sound' in globals(): gameover_sound.play()
            save_high_score(length - 1)
            return

        screen.fill(black)
        pygame.draw.rect(screen, red, [foodx, foody, block, block])

        head = [x, y]
        snake.append(head)
        if len(snake) > length:
            del snake[0]

        if head in snake[:-1]:
            if 'gameover_sound' in globals(): gameover_sound.play()
            save_high_score(length - 1)
            return

        draw_snake(block, snake)
        show_score(max(0, length - 3), high_score)

        pygame.display.update()

        if x == foodx and y == foody:
            foodx = round(random.randrange(0, width - block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - block) / 10.0) * 10.0
            length += 1
            speed += 0.5
            if 'eat_sound' in globals(): eat_sound.play()

        clock.tick(speed)

# Run the game
while True:
    start_menu()
    game_loop()
