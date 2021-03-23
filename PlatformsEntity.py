import VectorClass

class Platform(VectorClass.Vector):
    def __init__(self, sprite, frame_width, frame_height):
        self.platform_dimensions = sprite.dest_size
        super().__init__(sprite)

        self.frame_width = frame_width
        self.frame_height = frame_height

    def update(self, canvas):
        self.movement_sprite.draw(canvas, super().get_p(), 0)