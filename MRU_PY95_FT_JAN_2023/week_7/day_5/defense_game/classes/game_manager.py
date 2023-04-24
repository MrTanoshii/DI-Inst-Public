import random

import pygame
from pygame.locals import *

from classes.asteroid import Asteroid
from classes.player import Player
from constants import Constants as C


class GameManager:
    def __init__(self):
        self.player = Player(C.Player.spawn_position)
        self.asteroid_list = []
        self.spawn_cooldown = random.uniform(
            C.GameManager.spawn_cooldown_range[0],
            C.GameManager.spawn_cooldown_range[1],
        )
        self.ticks_since_last_frame = pygame.time.get_ticks()
        self.game_ended = False

        pygame.mixer.Sound("defense_game/assets/bgm/Retro Ambience Short 09.wav").play(
            -1
        )

        self.score = 1000
        self.highscore = self.score

    def update(self, display_surface):
        # Clear the screen
        display_surface.fill((0, 0, 0))

        if self.game_ended:
            # Display game over
            font = pygame.font.Font("freesansbold.ttf", 48)
            text = font.render(f"Game Over", True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (C.Window.resolution[0] // 2, C.Window.resolution[1] // 2)
            display_surface.blit(text, textRect)

            # Display highscore
            font = pygame.font.Font("freesansbold.ttf", 32)
            text = font.render(
                f"Highscore: {self.highscore:.0f}", True, (255, 255, 255)
            )
            textRect = text.get_rect()
            textRect.center = (
                C.Window.resolution[0] // 2,
                (C.Window.resolution[1] // 2) + 50,
            )
            display_surface.blit(text, textRect)
            return

        # End the game
        if self.player and self.player.died:
            self.game_ended = True
            self.player.kill()
            self.player = None
        elif self.player:
            # Update the player and asteroids
            self.player.update()

            for bullet in self.player.bullet_list:
                bullet.update()
                if bullet.despawn:
                    self.despawn_bullet(bullet)
            for asteroid in self.asteroid_list:
                asteroid.update()

                # Increase score when destroying asteroid
                if asteroid.died:
                    self.score += asteroid.score_value

                    # Update the highscore
                    if self.highscore < self.score:
                        self.highscore = self.score

                if asteroid.despawn:
                    if not asteroid.died:
                        pygame.mixer.Sound(
                            "defense_game/assets/sfx/Retro Weird Psych 05.wav"
                        ).play(0).set_volume(0.3)
                        self.score -= asteroid.score_value
                        if self.score < 0:
                            self.game_ended = True
                    self.despawn_asteroid(asteroid)
                else:
                    asteroid.check_collided_with(self.player)
                    if asteroid.collided_with_player:
                        self.player.take_damage(1)
                        self.despawn_asteroid(asteroid)

                    for bullet in self.player.bullet_list:
                        if asteroid.check_collided_with(bullet):
                            self.despawn_bullet(bullet)

            # Update the display
            display_surface.blit(self.player.image, self.player.rect)
            for bullet in self.player.bullet_list:
                display_surface.blit(bullet.surf, bullet.rect)
            for asteroid in self.asteroid_list:
                display_surface.blit(asteroid.surf, asteroid.rect)

            # Display score
            font = pygame.font.Font("freesansbold.ttf", 24)
            text = font.render(f"Score: {self.score:.0f}", True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (C.Window.resolution[1] - 200, 34)
            display_surface.blit(text, textRect)

            # Calculate the delta time
            t = pygame.time.get_ticks()
            delta_time = (t - self.ticks_since_last_frame) / 1000.0  # In seconds
            self.ticks_since_last_frame = t

            self.spawn_cooldown -= delta_time
            if len(self.asteroid_list) < C.GameManager.max_asteroids:
                if self.spawn_cooldown <= 0:
                    self.spawn_cooldown = random.uniform(
                        C.GameManager.spawn_cooldown_range[0],
                        C.GameManager.spawn_cooldown_range[1],
                    )
                    self.spawn_asteroid()

    def spawn_asteroid(self):
        size = random.randint(C.Asteroid.size_range[0], C.Asteroid.size_range[1])
        spawn_position = (random.randint(0, C.Window.resolution[0]), size / 2)
        fall_speed = random.uniform(
            C.Asteroid.fall_speed_range[0], C.Asteroid.fall_speed_range[1]
        )
        self.asteroid_list.append(Asteroid(spawn_position, (size, size), fall_speed))

    def despawn_asteroid(self, asteroid):
        self.asteroid_list.remove(asteroid)
        asteroid.kill()

    def end_screen(self):
        pass

    def despawn_bullet(self, bullet):
        self.player.bullet_list.remove(bullet)
        bullet.kill()
