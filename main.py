import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Let's Level Up the Game!")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Sprite setup
class ColorChangingSprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.color = color
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def change_color(self):
        # Change to a random color
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.image.fill(self.color)

# Define sprite dimensions and initial positions
sprite1 = ColorChangingSprite((255, 0, 0), 50, 50, WIDTH // 4, HEIGHT // 2)
sprite2 = ColorChangingSprite((0, 0, 255), 50, 50, 3 * WIDTH // 4, HEIGHT // 2)

# Grouping the sprites for easier collision management
all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1)
all_sprites.add(sprite2)

# Custom event to change color when sprites collide
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CHANGE_COLOR_EVENT:
            sprite1.change_color()
            sprite2.change_color()

    # Check for collision between sprites and trigger custom event
    if pygame.sprite.collide_rect(sprite1, sprite2):
        pygame.event.post(pygame.event.Event(CHANGE_COLOR_EVENT))

    # Update and draw sprites
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()