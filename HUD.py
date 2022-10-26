import pygame


class Hud(pygame.sprite.Sprite):
    def __init__(self):

        self.current = 0
        self.sprites = []
        self.sprites.append(pygame.image.load('Sprites/itens/botão HUD.png'))
        self.sprites.append(pygame.image.load('Sprites/itens/botão HUD (1).png'))
        self.image = self.sprites[self.current]
        self.animation = False

    def update(self):
        self.animation = True
        if self.animation == True:
            display_surface = pygame.display.get_surface()
            self.rect = self.image.get_rect(bottomleft = (10, 640))
            self.current = self.current + 0.1
            if self.current >= len(self.sprites):
                self.current = 0
        self.image = self.sprites[int(self.current)]
        self.image = pygame.transform.scale(self.image, (32 * 4, 32 * 4))
        display_surface.blit(self.image, self.rect)
