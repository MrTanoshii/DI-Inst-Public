import pygame

from classes.bullet import Bullet
from classes.player import Player
from constants import Constants as C


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, spawn_position, size, fall_speed):
        super().__init__()
        self.surf = pygame.Surface(size)
        self.surf.fill((255, 69, 0))
        self.rect = self.surf.get_rect(center=(size[0] / 2, size[1] / 2))
        self.pos = spawn_position
        self.rect.center = self.pos
        self.fall_speed = fall_speed
        self.despawn = False
        self.collided_with_player = False
        self.health = (size[0] / C.Asteroid.size_range[1]) * C.Asteroid.health_max
        self.died = False
        self.score_value = (size[0] / C.Asteroid.size_range[1]) * C.Asteroid.score_max

    def update(self):
        self.pos = (self.pos[0], self.pos[1] + self.fall_speed)
        self.rect.center = self.pos

        # Out of screen
        if self.rect.top > C.Window.resolution[1]:
            self.despawn = True

        # Dead
        elif self.died:
            self.despawn = True

            # Play sfx
            pygame.mixer.Sound(
                "defense_game/assets/sfx/Retro Gun Laser SingleShot 01.wav"
            ).play(0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def check_collided_with(self, other):
        if self.rect.colliderect(other.rect):
            if type(other) == Player:
                self.collided_with_player = True

                # Play sfx
                pygame.mixer.Sound("defense_game/assets/sfx/Retro Impact 20.wav").play(
                    0
                )
                return True
            elif type(other) == Bullet:
                self.take_damage(other.damage_value)

                # Play sfx
                pygame.mixer.Sound("defense_game/assets/sfx/Retro Swooosh 07.wav").play(
                    0
                )

                return True

        return False

    def take_damage(self, damage_value):
        self.health -= damage_value
        if self.health <= 0:
            self.died = True

            # Play sfx
            pygame.mixer.Sound(
                "defense_game/assets/sfx/Retro Explosion Short 15.wav"
            ).play(0)
