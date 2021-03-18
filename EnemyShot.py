import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import VectorClass


class enemyShot(VectorClass.Vector):
    delay = 0
    radius = 0
    remove_request = False

    def __init__(self, delay, radius, position):
        self.delay = delay
        self.radius = radius
        super().__init__(position[0], position[1])

    def update(self, canvas):
        if self.delay == 0:
            canvas.draw_circle(super().get_p(), self.radius, 1, "black", "red")
        elif self.delay == -1:
            self.remove_request = True
        else:
            canvas.draw_circle(super().get_p(), self.radius, 1, "black")
            self.delay -= 1
