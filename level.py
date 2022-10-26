import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *



class Level():
    def __init__(self):
        super().__init__()
        #display surface
        self.display_surface = pygame.display.get_surface()

        #sprite group
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.door_sprites = pygame.sprite.Group()


        self.level = pygame.image.load('Sprites/levels/1/level1.png')


        #sprite setup
        self.create_map()


    def run(self):
        #updatedraw
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()



    def create_map(self):
        layouts = {'boundary': import_csv_layout('C:/Users/souza/PycharmProjects/pythonProject3/Sprites/levels/0/level0_constraint.csv'),
            'door 1': import_csv_layout('C:/Users/souza/PycharmProjects/pythonProject3/Sprites/levels/0/level0_door 1.csv')
        }

        self.player = Player((300, 600), [self.visible_sprites], self.obstacle_sprites, self.door_sprites)
        for style, layout in layouts.items():
            for row_index, row in enumerate (layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x,y),[self.obstacle_sprites],'invisible')
                        if style == 'door 1':
                            Tile((x,y),[self.door_sprites],'door 1')
                            for sprite in self.door_sprites:
                                if sprite.hitbox.colliderect(self.player):
                                   print(funciona)
           #     if col == 'x':
            #        Tile((x,y),[self.visible_sprites, self.obstacle_sprites])
             #   if col == 'p':
                    #self.player = Player((x,y), [self.visible_sprites],self.obstacle_sprites)




class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        #setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        #chão
        self.floor_surf = pygame.image.load('Sprites/levels/0/level0.png').convert()
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