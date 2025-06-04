import pygame
import random

WIDTH, HEIGHT = 800, 300
GROUND_HEIGHT = 250

class Unicorn:
    def __init__(self):
        # create a surface with transparency for a more detailed sprite
        self.image = pygame.Surface((80, 60), pygame.SRCALPHA)
        body_color = (255, 255, 255)
        mane_color = (255, 180, 255)

        # body and head
        pygame.draw.ellipse(self.image, body_color, (20, 25, 40, 25))
        pygame.draw.circle(self.image, body_color, (60, 30), 12)

        # horn
        pygame.draw.polygon(self.image, (255, 215, 0), [(68, 15), (72, 0), (76, 15)])

        # legs
        pygame.draw.rect(self.image, body_color, (25, 45, 8, 15))
        pygame.draw.rect(self.image, body_color, (45, 45, 8, 15))

        # tail
        pygame.draw.polygon(self.image, mane_color, [(20, 35), (10, 30), (10, 40)])

        # mane
        pygame.draw.rect(self.image, mane_color, (55, 20, 5, 10))

        self.rect = self.image.get_rect()
        self.rect.left = 50
        self.rect.bottom = GROUND_HEIGHT
        self.y_speed = 0

    def update(self, keys):
        if keys[pygame.K_UP]:
            self.y_speed = -6  # flap wings
        elif keys[pygame.K_DOWN]:
            self.y_speed += 1.5  # stomp down
        else:
            self.y_speed += 0.5  # gravity
        self.rect.y += int(self.y_speed)
        if self.rect.bottom > GROUND_HEIGHT:
            self.rect.bottom = GROUND_HEIGHT
            self.y_speed = 0
        if self.rect.top < 0:
            self.rect.top = 0
            self.y_speed = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Star:
    def __init__(self):
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.left = WIDTH
        self.rect.y = random.randint(20, GROUND_HEIGHT - 60)

    def update(self):
        self.rect.x -= 4

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def off_screen(self):
        return self.rect.right < 0

class Princess:
    def __init__(self):
        self.image = pygame.Surface((30, 50), pygame.SRCALPHA)
        # dress
        pygame.draw.rect(self.image, (255, 105, 180), (5, 20, 20, 30))
        # head
        pygame.draw.circle(self.image, (255, 224, 189), (15, 10), 10)
        self.rect = self.image.get_rect()
        self.rect.left = WIDTH
        self.rect.bottom = GROUND_HEIGHT

    def update(self):
        self.rect.x -= 3

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def off_screen(self):
        return self.rect.right < 0

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Unicorn Adventure")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)

    unicorn = Unicorn()
    stars = []
    princesses = []
    score = 0
    princess_score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if random.randint(0, 90) == 0:
            stars.append(Star())
        if random.randint(0, 500) == 0:
            princesses.append(Princess())

        for star in list(stars):
            star.update()
            if star.off_screen():
                stars.remove(star)
            elif unicorn.rect.colliderect(star.rect):
                stars.remove(star)
                score += 1

        for princess in list(princesses):
            princess.update()
            if princess.off_screen():
                princesses.remove(princess)
            elif unicorn.rect.colliderect(princess.rect):
                princesses.remove(princess)
                princess_score += 1

        unicorn.update(keys)

        screen.fill((135, 206, 235))
        pygame.draw.rect(screen, (50, 205, 50), (0, GROUND_HEIGHT, WIDTH, HEIGHT - GROUND_HEIGHT))

        unicorn.draw(screen)
        for star in stars:
            star.draw(screen)
        for princess in princesses:
            princess.draw(screen)

        score_text = font.render(
            f"Stars: {score}  Princesses: {princess_score}", True, (0, 0, 0)
        )
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
