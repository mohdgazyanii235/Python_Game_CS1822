import Player
import Entity

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Clock:
    frame_duration = 1

    def __init__(self):
        self.time = 0
        frame_duration = 1

    def tick(self):
        self.time += 1

    def transition(self, frame_duration):
        if self.tick == frame_duration:
            return True


WIDTH = 1000
HEIGHT = 700

entities = []

frame = simplegui.create_frame("Game Name Placeholder", WIDTH, HEIGHT)
Clock()

# Spritesheet(SpriteURL, X, Y, columns, rows, frame_duration, location on canvas, Cell size, Number of animation cells
# (to loop animation w/o white frames))

player = Entity.Entity(
    "https://i.imgur.com/wp1QgXP.png", 4, 8, Clock.frame_duration, (WIDTH / 2, HEIGHT / 2), (300, 120), 30
)

entities.append(player)


def draw_entities(canvas):
    for entity in entities:
        entity.draw(canvas)


frame.set_canvas_background('white')
frame.set_draw_handler(draw_entities)

frame.start()

