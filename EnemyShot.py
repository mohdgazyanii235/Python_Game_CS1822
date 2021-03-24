import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import VectorClass


class enemyShot(VectorClass.Vector):
    delay = 0
    radius = 0
    remove_request = False
    is_detonated = False

    def __init__(self, delay, radius, position):
        self.delay = delay
        self.radius = radius
        super().__init__(position[0], position[1])

    def update(self, canvas):
        if self.delay <= 0:
            canvas.draw_circle(super().get_p(), self.radius, 1, "black", "white")
            self.radius *= 0.8
            self.is_detonated = True
        else:
            canvas.draw_circle(super().get_p(), self.radius, 1, "black")

        self.delay -= 1

        if self.delay == -20:
            self.remove_request = True
