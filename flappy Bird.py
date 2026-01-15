import pygame
import random
import sys

# Initialisierung
pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

# Farben
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLUE = (0, 150, 255)

# Vogel
bird_x = 80
bird_y = HEIGHT // 2
bird_radius = 15
gravity = 0.5
bird_movement = 0
jump_strength = -8

# Röhren
pipe_width = 60
pipe_gap = 150
pipe_speed = 3
pipes = []

def create_pipe():
    height = random.randint(100, 400)
    top = pygame.Rect(WIDTH, 0, pipe_width, height)
    bottom = pygame.Rect(WIDTH, height + pipe_gap, pipe_width, HEIGHT)
    return top, bottom

pipes.extend(create_pipe())

score = 0

def draw_text(text, x, y):
    img = font.render(text, True, WHITE)
    screen.blit(img, (x, y))

# Spielschleife
running = True
while running:
    clock.tick(60)
    screen.fill(BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = jump_strength

    # Vogel Physik
    bird_movement += gravity
    bird_y += bird_movement

    bird = pygame.Rect(bird_x - bird_radius, bird_y - bird_radius,
                       bird_radius * 2, bird_radius * 2)

    pygame.draw.circle(screen, WHITE, (bird_x, int(bird_y)), bird_radius)

    # Röhren bewegen
    for pipe in pipes:
        pipe.x -= pipe_speed
        pygame.draw.rect(screen, GREEN, pipe)

    # Neue Röhren
    if pipes[0].x < -pipe_width:
        pipes.pop(0)
        pipes.pop(0)
        pipes.extend(create_pipe())
        score += 1

    # Kollision
    for pipe in pipes:
        if bird.colliderect(pipe):
            running = False

    if bird_y < 0 or bird_y > HEIGHT:
        running = False

    draw_text(f"Score: {score}", 10, 10)
    pygame.display.update()

pygame.quit()
sys.exit()
