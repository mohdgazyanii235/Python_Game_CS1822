import PlatformsEntity

class Platforms(PlatformsEntity.Platform):
    def __init__(self, enemy_human_sprite, frame_width, frame_height, speed):
        super().__init__(enemy_human_sprite, frame_width, frame_height, speed)

    def update(self, canvas):
        super().update(canvas)