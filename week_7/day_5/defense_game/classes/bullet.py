import pygame

from constants import Constants as C


class Bullet(pygame.sprite.Sprite):
    def __init__(self, spawn_position, velocity):
        super().__init__()
        self.surf = pygame.Surface(C.Bullet.size)
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(
            center=(C.Bullet.size[0] / 2, C.Bullet.size[1] / 2)
        )
        self.pos = spawn_position
        self.rect.center = self.pos
        self.despawn = False
        self.velocity = velocity
        self.damage_value = C.Bullet.damage_value

        # Play sfx
        pygame.mixer.Sound(
            "defense_game/assets/sfx/Retro Gun Laser SingleShot 01.wav"
        ).play(0)

    def update(self):
        # Move the bullet
        self.pos = (self.pos[0] + self.velocity[0], self.pos[1] + self.velocity[1])
        self.rect.center = self.pos

        if (
            self.rect.top > C.Window.resolution[1]
            or self.rect.left > C.Window.resolution[0]
        ):
            self.despawn = True
