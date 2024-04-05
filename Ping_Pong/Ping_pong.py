

import pygame
from pygame.locals import *

# Sizes of screen
WIDTH = 800
HEIGHT = 400

# Player attributes
PLAYER_WIDTH = 10
PLAYER_HEIGHT = 60
PLAYER_SPEED = 5

# Players speed
player1_speed = 0
player2_speed = 0

# Player positions
player1_pos = [10, HEIGHT // 2 - PLAYER_HEIGHT // 2]
player2_pos = [WIDTH - 10 - PLAYER_WIDTH, HEIGHT // 2 - PLAYER_HEIGHT // 2]

# Ball attributes
BALL_RADIUS = 6
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_dir = [-1, 1]
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Player scores
player1_score = 0
player2_score = 0

# Creating screen
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Running code
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        # Getting inputted values
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Indicating scores, players positions and balls position
                player1_score = 0
                player2_score = 0
                player1_pos = [10, HEIGHT // 2 - PLAYER_HEIGHT // 2]
                player2_pos = [WIDTH - 10 - PLAYER_WIDTH, HEIGHT // 2 - PLAYER_HEIGHT // 2]
                ball_pos = [WIDTH // 2, HEIGHT // 2]
                ball_dir = [-1, 1]

    # Moving player 1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1_speed = -PLAYER_SPEED
    elif keys[pygame.K_s]:
        player1_speed = PLAYER_SPEED
    else:
        player1_speed = 0

    # Moving player 2
    if keys[pygame.K_UP]:
        player2_speed = -PLAYER_SPEED
    elif keys[pygame.K_DOWN]:
        player2_speed = PLAYER_SPEED
    else:
        player2_speed = 0

    player1_pos[1] += player1_speed
    player2_pos[1] += player2_speed

    # Positioning player 1
    if player1_pos[1] < 0:
        player1_pos[1] = 0
    elif player1_pos[1] > HEIGHT - PLAYER_HEIGHT:
        player1_pos[1] = HEIGHT - PLAYER_HEIGHT

    # Positioning player 2
    if player2_pos[1] < 0:
        player2_pos[1] = 0
    elif player2_pos[1] > HEIGHT - PLAYER_HEIGHT:
        player2_pos[1] = HEIGHT - PLAYER_HEIGHT

    # Ball moving
    ball_pos[0] += BALL_SPEED_X * ball_dir[0]
    ball_pos[1] += BALL_SPEED_Y * ball_dir[1]

    # Ball collision with players
    if ball_pos[0] <= player1_pos[0] + PLAYER_WIDTH and \
            player1_pos[1] <= ball_pos[1] <= player1_pos[1] + PLAYER_HEIGHT:
        ball_dir[0] = 1
    elif ball_pos[0] >= player2_pos[0] - BALL_RADIUS and \
            player2_pos[1] <= ball_pos[1] <= player2_pos[1] + PLAYER_HEIGHT:
        ball_dir[0] = -1

    # Ball collision with walls
    if ball_pos[1] <= 0 or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_dir[1] = -ball_dir[1]

    # PLayer 2 scoring
    if ball_pos[0] < 0:
        player2_score += 1
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        ball_dir = [-1, 1]

    # Player 1 scoring
    elif ball_pos[0] > WIDTH - BALL_RADIUS:
        player1_score += 1
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        ball_dir = [1, 1]

    # filling screen with black color
    window.fill((0, 0, 0))

    # drawing all shapes
    pygame.draw.rect(window, (2, 170, 255), (player1_pos[0], player1_pos[1], PLAYER_WIDTH, PLAYER_HEIGHT))
    pygame.draw.rect(window, (255, 0, 81), (player2_pos[0], player2_pos[1], PLAYER_WIDTH, PLAYER_HEIGHT))
    pygame.draw.circle(window, (221, 144, 254), (ball_pos[0], ball_pos[1]), BALL_RADIUS)
    pygame.draw.aaline(window, (2, 202, 151), (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Showing score of the players
    font = pygame.font.Font(None, 36)
    player1_score_text = font.render(str(player1_score), True, (2, 170, 255))
    player2_score_text = font.render(str(player2_score), True, (255, 0, 81))
    window.blit(player1_score_text, (WIDTH // 2 - 50, 10))
    window.blit(player2_score_text, (WIDTH // 2 + 40, 10))

    if player1_score == 3:
        font = pygame.font.Font(None, 36)
        player1_winning_text = font.render(str("Player 1 won"), True, (2, 170, 255))
        window.blit(player1_winning_text, (WIDTH // 2 - 50, 10))
        running = False
    if player2_score == 3:
        font = pygame.font.Font(None, 36)
        player2_winning_text = font.render(str("Player 2 won"), True, (2, 170, 255))
        window.blit(player2_winning_text, (WIDTH // 2 - 50, 10))
        running = False

    # Show all work
    pygame.display.flip()
    clock.tick(60)

# Quit the program
pygame.quit()