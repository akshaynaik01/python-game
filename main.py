import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Clock for FPS
CLOCK = pygame.time.Clock()
FPS = 10

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
    
    def update(self):
        self.x += self.dx
        self.y += self.dy
        
        # Wrap around screen
        if self.x < 0:
            self.x = SCREEN_WIDTH - GRID_SIZE
        elif self.x >= SCREEN_WIDTH:
            self.x = 0
        
        if self.y < 0:
            self.y = SCREEN_HEIGHT - GRID_SIZE
        elif self.y >= SCREEN_HEIGHT:
            self.y = 0
    
    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, GRID_SIZE, GRID_SIZE))

class Food:
    def __init__(self):
        self.x = random.randint(0, (SCREEN_WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        self.y = random.randint(0, (SCREEN_HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
    
    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, GRID_SIZE, GRID_SIZE))

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Python Game - Arrow Keys to Move")
    
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    food = Food()
    score = 0
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.dx = 0
                    player.dy = -GRID_SIZE
                elif event.key == pygame.K_DOWN:
                    player.dx = 0
                    player.dy = GRID_SIZE
                elif event.key == pygame.K_LEFT:
                    player.dx = -GRID_SIZE
                    player.dy = 0
                elif event.key == pygame.K_RIGHT:
                    player.dx = GRID_SIZE
                    player.dy = 0
        
        player.update()
        
        # Check collision with food
        if player.x == food.x and player.y == food.y:
            score += 10
            food = Food()
        
        # Draw
        screen.fill(BLACK)
        player.draw(screen)
        food.draw(screen)
        
        # Draw score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, YELLOW)
        screen.blit(score_text, (10, 10))
        
        pygame.display.flip()
        CLOCK.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
