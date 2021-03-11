try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Spritesheet:
    def __init__(self,
                 imgurl,
                 columns, rows,
                 frame_duration,
                 dest_centre, dest_size, cells, loop):

        self.img = simplegui._load_local_image(imgurl)
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.columns = columns
        self.rows = rows
        self.frame_duration = frame_duration
        self.dest_centre = dest_centre
        self.dest_size = dest_size
        self.cells = cells
        self.loop = loop
        self.cell_count = 0
        self.frame_width = self.width / columns
        self.frame_height = self.height / rows
        self.frame_centre_x = self.frame_width / 2
        self.frame_centre_y = self.frame_height / 2

        self.frame_index = [0, 0]
        self.frame_clock = 0

    def update_index(self):
        self.cell_count += 1
        if not self.loop:
            if self.cell_count == self.cells:
                self.dest_size = (0, 0)
        if self.cell_count == self.cells:
            self.cell_count = 1
            self.frame_index[0] = 0
            self.frame_index[1] = 0
        self.frame_index[0] = (self.frame_index[0] + 1) % self.columns
        if self.frame_index[0] == 0:
            self.frame_index[1] = (self.frame_index[1] + 1) % self.rows

    def draw(self, canvas, position, rotation):
        self.frame_clock += 1
        if self.frame_clock % self.frame_duration == 0:
            self.update_index()

        source_centre = (
            self.frame_width * self.frame_index[0] + self.frame_centre_x,
            self.frame_height * self.frame_index[1] + self.frame_centre_y
        )

        source_size = (self.frame_width, self.frame_height)

        canvas.draw_image(self.img, source_centre, source_size, position, self.dest_size, rotation)
