import pygame
from pygame.locals import *

from classes.bullet import Bullet
from constants import Constants as C


class Player(pygame.sprite.Sprite):
    def __init__(self, spawn_position):
        super().__init__()

        self.images = [
            self.load_image("defense_game/assets/art/l0_SpaceShip0011.png"),
            self.load_image("defense_game/assets/art/l0_SpaceShip0012.png"),
            self.load_image("defense_game/assets/art/l0_SpaceShip0013.png"),
            self.load_image("defense_game/assets/art/l0_SpaceShip0014.png"),
            self.load_image("defense_game/assets/art/l0_SpaceShip0015.png"),
            self.load_image("defense_game/assets/art/l0_SpaceShip0016.png"),
        ]

        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect(center=spawn_position)
        self.health = C.Player.health
        self.died = False
        self.weapon = C.Player.weapon
        self.shoot_cooldown = C.Player.weapon_cooldown
        self.bullet_list = []
        self.ticks_since_last_frame = pygame.time.get_ticks()

    def update(self):
        self.image_index = (self.image_index + 1) % len(self.images)
        self.image = self.images[self.image_index]

        t = pygame.time.get_ticks()
        delta_time = (t - self.ticks_since_last_frame) / 1000.0  # In seconds
        self.ticks_since_last_frame = t

        self.shoot_cooldown -= delta_time

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[C.Hotkey.move_left] and self.rect.left > 0:
            self.rect.move_ip(-C.Player.movement_speed, 0)
        elif (
            pressed_keys[C.Hotkey.move_right]
            and self.rect.right < C.Window.resolution[0]
        ):
            self.rect.move_ip(C.Player.movement_speed, 0)
        elif pressed_keys[C.Hotkey.shoot] and self.shoot_cooldown <= 0:
            self.shoot()
            self.shoot_cooldown = C.Player.weapon_cooldown

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def take_damage(self, damage_value):
        self.health -= damage_value
        if self.health <= 0:
            self.died = True

    def shoot(self):
        self.bullet_list.append(Bullet(self.rect.center, (0, -1)))

    def load_image(self, image_path):
        return pygame.image.load(image_path)
