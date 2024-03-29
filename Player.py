import DroneEntity
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Player(DroneEntity.Drone):

    moving_left = False
    moving_right = False
    moving_up = False
    moving_down = False

    queued_direction = ""
    exit_request = False
    size_multiplier = 1

    is_firing = False

    lives = 3

    reload_time = 20
    reload_progress = 20

    grace_period = 50
    current_grace = 50
    is_invulnerable = False

    def __init__(self, player_sprite, frame_width, frame_height, speed):

        super().__init__(player_sprite, frame_width, frame_height, speed)

    def update(self, canvas):

        if self.current_grace < self.grace_period:
            self.is_invulnerable = True
            self.current_grace += 1
        else:
            self.is_invulnerable = False

        super().update(canvas, self.moving_left, self.moving_right, self.moving_up, self.moving_down)

        if self.reload_progress < self.reload_time:
            self.reload_progress += 1
            if self.reload_progress <= self.reload_time / 2:
                self.movement_sprite.change_size(1/0.99)
            else:
                self.movement_sprite.change_size(0.99)


    def keyDown(self, key):
        if key == simplegui.KEY_MAP['left']:
            if not self.moving_right:
                self.moving_left = True
            else:
                self.queued_direction = "left"
                # If the player is currently moving right it will queue moving left

        if key == simplegui.KEY_MAP['right']:
            if not self.moving_left:
                self.moving_right = True
            else:
                self.queued_direction = "right"

        if key == simplegui.KEY_MAP['up']:
            self.moving_up = True

        if key == simplegui.KEY_MAP['down']:
            self.moving_down = True

    def get_exit_request(self):
        return self.exit_request

    def take_damage(self):
        if not self.is_invulnerable:
            self.lives -= 1
            if self.lives == 0:
                self.remove_request = True
            else:
                self.current_grace = 0

    def fire(self):
        if self.reload_progress == self.reload_time:
            self.is_firing = True
            self.reload_progress = 0

    def keyUp(self, key):

        if key == simplegui.KEY_MAP['left']:
            if self.queued_direction == "left":
                self.queued_direction = ""
                # If the key is released then remove it from the queue, as otherwise you could tap left whilst moving
                # right, yet once the right key is released left will still be queued, moving the player left

            elif self.queued_direction == "right":
                self.moving_left = False
                self.moving_right = True
                self.queued_direction = ""
                # If key is released and right is queued, change player direction to right

            else:
                self.moving_left = False
                self.skid_value = -self.speed
                # If key is released and right is not queued, then stop the player's movement

        if key == simplegui.KEY_MAP['right']:
            if self.queued_direction == "right":
                self.queued_direction = ""

            elif self.queued_direction == "left":
                self.moving_right = False
                self.moving_left = True
                self.queued_direction = ""

            else:
                self.moving_right = False
                self.rotation = 0
                self.skid_value = self.speed

        if key == simplegui.KEY_MAP['up']:
            self.moving_up = False

        if key == simplegui.KEY_MAP['down']:
            self.moving_down = False

        if key == simplegui.KEY_MAP['space']:
            self.fire()

        if key == simplegui.KEY_MAP['x']:
            self.exit_request = True
