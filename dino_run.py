import pygame
import random

WIDTH, HEIGHT = 800, 200
GROUND_HEIGHT = 150

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Run")
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 36)

class Dino:
    def __init__(self):
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.bottom = GROUND_HEIGHT
        self.rect.left = 50
        self.is_jumping = False
        self.jump_speed = 0

    def update(self):
        if self.is_jumping:
            self.rect.y += self.jump_speed
            self.jump_speed += 1  # gravity
            if self.rect.bottom >= GROUND_HEIGHT:
                self.rect.bottom = GROUND_HEIGHT
                self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.jump_speed = -15

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Obstacle:
    def __init__(self, x):
        self.image = pygame.Surface((20, 40))
        self.image.fill((34, 177, 76))
        self.rect = self.image.get_rect()
        self.rect.bottom = GROUND_HEIGHT
        self.rect.left = x

    def update(self):
        self.rect.x -= 5

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def off_screen(self):
        return self.rect.right < 0

def main():
    dino = Dino()
    obstacles = []
    score = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                dino.jump()

        if random.randint(0, 90) == 0:
            obstacles.append(Obstacle(WIDTH))

        for ob in list(obstacles):
            ob.update()
            if ob.off_screen():
                obstacles.remove(ob)
                score += 1

        dino.update()

        screen.fill((255, 255, 255))
        pygame.draw.line(screen, (128, 128, 128), (0, GROUND_HEIGHT), (WIDTH, GROUND_HEIGHT), 2)

        dino.draw(screen)
        for ob in obstacles:
            ob.draw(screen)

        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        for ob in obstacles:
            if dino.rect.colliderect(ob.rect):
                running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
