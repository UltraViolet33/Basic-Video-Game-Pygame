import pygame


class Enemy:
    def __init__(self):
        self.enemy_img = pygame.image.load("./assets/enemy.png")
        self.enemy_img_rect = self.enemy_img.get_rect()
        self.enemy_img_rect.top = 300
        self.enemy_img_rect.right = 1200
        self.up = True
        self.down = False
        self.velocity = 10

    def update(self, window, limit_top, limit_bottom):
        window.blit(self.enemy_img, self.enemy_img_rect)

        if self.enemy_img_rect.top < limit_top.y:
            self.up = False
            self.down = True

        elif self.enemy_img_rect.bottom > limit_bottom.y:
            self.down = False
            self.up = True

        if self.up:
            self.enemy_img_rect.top -= self.velocity
        elif self.down:
            self.enemy_img_rect.top += self.velocity
