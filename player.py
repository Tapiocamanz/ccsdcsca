import pygame
from settings import *
from HUD import Hud
from level import *


class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obstacle_sprites,door_sprites,ii, passing):
        super().__init__(groups)
        self.current = 0
        self.sprites = []
        self.sprites_stopped_l = []
        self.sprites_up = []
        self.sprites_down = []
        self.sprites_left = []
        self.sprites_right = []
        self.sprites.append(pygame.image.load('Sprites/personagens/personagem.png'))
        self.sprites_right.append(pygame.image.load('Sprites/personagens/walking 1.png'))
        self.sprites_right.append(pygame.image.load('Sprites/personagens/walking 2.png'))
        self.sprites_right.append(pygame.image.load('Sprites/personagens/walking 3.png'))
        self.sprites_right.append(pygame.image.load('Sprites/personagens/walking 4.png'))
        self.sprites_right.append(pygame.image.load('Sprites/personagens/walking 5.png'))
        self.sprites_right.append(pygame.image.load('Sprites/personagens/walking 6.png'))
        self.sprites_left.append(pygame.image.load('Sprites/personagens/walking 2L.png'))
        self.sprites_left.append(pygame.image.load('Sprites/personagens/walking 3L.png'))
        self.sprites_left.append(pygame.image.load('Sprites/personagens/walking 4 L.png'))
        self.sprites_left.append(pygame.image.load('Sprites/personagens/walking 5L.png'))
        self.sprites_left.append(pygame.image.load('Sprites/personagens/walking 6L.png'))
        self.sprites_up.append(pygame.image.load('Sprites/personagens/walking 1.png'))
        self.sprites_up.append(pygame.image.load('Sprites/personagens/walking 2.png'))
        self.sprites_up.append(pygame.image.load('Sprites/personagens/walking 3.png'))
        self.sprites_up.append(pygame.image.load('Sprites/personagens/walking 4.png'))
        self.sprites_up.append(pygame.image.load('Sprites/personagens/walking 5.png'))
        self.sprites_up.append(pygame.image.load('Sprites/personagens/walking 6.png'))
        self.sprites_down.append(pygame.image.load('Sprites/personagens/walking 1.png'))
        self.sprites_down.append(pygame.image.load('Sprites/personagens/walking 2.png'))
        self.sprites_down.append(pygame.image.load('Sprites/personagens/walking 3.png'))
        self.sprites_down.append(pygame.image.load('Sprites/personagens/walking 4.png'))
        self.sprites_down.append(pygame.image.load('Sprites/personagens/walking 5.png'))
        self.sprites_down.append(pygame.image.load('Sprites/personagens/walking 6.png'))
        self.image = self.sprites[self.current]
        self.image = pygame.transform.scale(self.image, (320-120, 320-120))
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-10, -10)
        self.animation = False

        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.door_sprites = door_sprites
        self.obstacle_sprites = obstacle_sprites
        self.hud = Hud()
        self.pressing_e = False
        self.passing = passing
        self.passing = False

    def idle(self):
        if self.animation == False:
            self.current = 0
            self.image = self.sprite[self.current]
            self.image = pygame.transform.scale(self.image, (320 - 120, 320 - 120))

    def walk_right(self):
        self.animation = True
        if self.animation == True:
            self.current = self.current + 0.1
            if self.current >= len(self.sprites_right):
                self.current = 0
                self.animation = False
        self.image = self.sprites_right[int(self.current)]
        self.image = pygame.transform.scale(self.image, (320 - 120, 320 - 120))

    def walk_left(self):
        self.animation = True
        if self.animation == True:
            self.current = self.current + 0.1
            if self.current >= len(self.sprites_left):
                self.current = 0
                self.animation = False
        self.image = self.sprites_left[int(self.current)]
        self.image = pygame.transform.scale(self.image, (320 - 120, 320 - 120))

    def walk_down(self):
        self.animation = True
        if self.animation == True:
            self.current = self.current + 0.1
            if self.current >= len(self.sprites_down):
                self.current = 0
                self.animation = False
        self.image = self.sprites_down[int(self.current)]
        self.image = pygame.transform.scale(self.image, (320 - 120, 320 - 120))

    def walk_up(self):
        self.animation = True
        if self.animation:
            self.current = self.current + 0.1
            if self.current >= len(self.sprites_up):
                self.current = 0
                self.animation = False
        self.image = self.sprites_up[int(self.current)]
        self.image = pygame.transform.scale(self.image, (320 - 120, 320 - 120))

    def input(self):
            keys = pygame.key.get_pressed()

            if keys[pygame.K_w]:
                self.direction.y = -1
                self.walk_up()
            elif keys[pygame.K_s]:
                self.direction.y = 1
                self.walk_down()
            else:
                self.direction.y = 0
            if keys[pygame.K_a]:
                self.direction.x = -1
                self.walk_left()
            elif keys[pygame.K_d]:
                self.direction.x = 1
                self.walk_right()
            else:
                self.direction.x = 0
            if keys[pygame.K_e]:
                self.pressing_e = True
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    self.idle


    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center
        self.collision('door')

    def collision(self,direction):
        if direction =='horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: #going to the right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: #going left
                        self.hitbox.left = sprite.hitbox.right
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: #going down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: #going up
                        self.hitbox.top = sprite.hitbox.bottom
        if direction == 'door':
            for sprite in self.door_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    self.hud.update()
                    self.passing = True

    def update(self):
        self.input()
        self.move(self.speed)
