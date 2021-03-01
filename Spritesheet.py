try:
    import simplegui
except ImportError :
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
    


class Spritesheet:
    def __init__(self, 
                 imgurl, 
                 width, height, 
                 columns, rows,
                 frame_duration, 
                 dest_centre, dest_size, cells):
        self.img = simplegui.load_image(imgurl)
        self.width = width
        self.height = height
        self.columns = columns
        self.rows = rows
        self.frame_duration = frame_duration
        self.dest_centre = dest_centre
        self.dest_size = dest_size
        self.cells = cells
        self.cellcount = 0
        
        self.frame_width = width / columns
        self.frame_height = height / rows
        self.frame_centre_x = self.frame_width / 2
        self.frame_centre_y = self.frame_height / 2

        self.frame_index = [0, 0]
        self.frame_clock = 0

    def update_index(self):
        self.cellcount += 1
        if self.cellcount == self.cells:
            self.cellcount = 1
            self.frame_index[0] = 0
            self.frame_index[1] = 0
        self.frame_index[0] = (self.frame_index[0] + 1) % self.columns
        if self.frame_index[0] == 0:
            self.frame_index[1] = (self.frame_index[1] + 1) % self.rows

    def draw(self, canvas):
        self.frame_clock += 1
        if self.frame_clock % self.frame_duration == 0:
            self.update_index()
    
        source_centre = (
            self.frame_width * self.frame_index[0] + self.frame_centre_x,
            self.frame_height * self.frame_index[1] + self.frame_centre_y
        )
        
        source_size = (self.frame_width, self.frame_height)
    
        canvas.draw_image(self.img,
                            source_centre,
                            source_size,
                            self.dest_centre,
                            self.dest_size)                      

frame = simplegui.create_frame("Sprite", 600, 300)
Clock()

#Spritesheet(SpriteURL, X, Y, columns, rows, frame_duration, location on canvas, Cell size, Number of animation cells (to loop animation w/o white frames))
sheet = Spritesheet(
    "https://i.imgur.com/wp1QgXP.png",
    1200, 960,
    4, 8,
    Clock.frame_duration, (300, 150), (300, 120), 30
)
frame.set_canvas_background('white')
frame.set_draw_handler(sheet.draw)

frame.start()