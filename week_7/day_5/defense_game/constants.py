from pygame.locals import *


class Constants:
    class Window:
        resolution = (720, 720)
        title = "Hackathon #2 - Defense Game"
        fps = 60

    class Hotkey:
        quit = K_ESCAPE
        move_left = K_LEFT
        move_right = K_RIGHT
        shoot = K_SPACE

    class Player:
        spawn_position = (360, 650)
        size = (32, 21)
        movement_speed = 1.5
        health = 3
        weapon = "minigun"
        weapon_cooldown = 0.3

    class Asteroid:
        size_range = (25, 50)
        fall_speed_range = (0.1, 0.3)
        health_max = 4
        score_max = 100

    class GameManager:
        max_asteroids = 10
        spawn_cooldown_range = (0.5, 2)

    class Bullet:
        size = (5, 5)
        max_velocity = 5
        damage_value = 1
