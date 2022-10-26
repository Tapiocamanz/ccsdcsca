import pygame
from player import Player



class parada(Player):
    def __init__(self):
        Player.__init__(self)
        self.display_surface = pygame.display.get_surface()
        self.gay = XSortCameraGroup()
        self.anderson = pygame.sprite.Group()
        self.cu = pygame.sprite.Group()
        self.player = Player((300, 600), [self.gay], self.anderson, self.cu)

    def run(self):
        self.gay.custom_draw(self.player)
        self.gay.update()


class XSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        #setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        #chão
        self.floor_surf = pygame.image.load('Sprites/levels/1/level1.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

    def custom_draw(self, player):

        #distância
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        #draw do chão
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf,floor_offset_pos)

        #for sprite in self.sprites():
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)

    def run(self):
        self.gay.custom_draw(self.player)
        self.gay.update()