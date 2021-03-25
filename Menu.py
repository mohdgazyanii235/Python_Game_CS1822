import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Menu:
    selector = None
    selection_num = 0
    button_selected = False
    start_game_request = False
    exit_request = False
    selection_height = False

    def __init__(self, width, height):

        self.start_btn = simplegui._load_local_image("sprite_assets/menu_assets/PyGameStartBtn.png")
        self.manual_btn = simplegui._load_local_image("sprite_assets/menu_assets/PyGameManualBtn.png")
        self.highscore_btn = simplegui._load_local_image("sprite_assets/menu_assets/PyGameHighscoresBtn.png")
        self.retire_btn = simplegui._load_local_image("sprite_assets/menu_assets/PyGameRetireBtn.png")
        self.selector = simplegui._load_local_image("sprite_assets/menu_assets/PyGameMenuSelector.png")
        self.license_img = simplegui._load_local_image("sprite_assets/menu_assets/PyGameLicenseMessage.png")

        self.width = width
        self.height = height

    def update(self, canvas):
        button_dimensions = (self.start_btn.get_width(), self.start_btn.get_height())

        canvas.draw_image(self.start_btn, (button_dimensions[0] / 2, button_dimensions[1] / 2), button_dimensions,
                          (self.width / 2, self.height / 2 - 180), button_dimensions)

        canvas.draw_image(self.manual_btn, (button_dimensions[0] / 2, button_dimensions[1] / 2), button_dimensions,
                          (self.width / 2, self.height / 2 - 60), button_dimensions)

        canvas.draw_image(self.highscore_btn, (button_dimensions[0] / 2, button_dimensions[1] / 2), button_dimensions,
                          (self.width / 2, self.height / 2 + 60), button_dimensions)

        canvas.draw_image(self.retire_btn, (button_dimensions[0] / 2, button_dimensions[1] / 2), button_dimensions,
                          (self.width / 2, self.height / 2 + 180), button_dimensions)

        canvas.draw_image(self.license_img, (self.license_img.get_width()/2, self.license_img.get_height()/2),
                          (self.license_img.get_width(), self.license_img.get_height()),
                          (self.license_img.get_width()/2 + 10, self.height - self.license_img.get_height()/2 - 10),
                          (self.license_img.get_width(), self.license_img.get_height()))

        selector_dimensions = (self.selector.get_width(), self.selector.get_height())

        if self.selection_num == 0:
            self.selection_height = -180

            if self.button_selected:
                self.button_selected = False
                self.start_game_request = True

        elif self.selection_num == 1:
            self.selection_height = -60

        elif self.selection_num == 2:
            self.selection_height = 60

        elif self.selection_num == 3:

            self.selection_height = 180

            if self.button_selected:
                self.exit_request = True

        canvas.draw_image(self.selector, (selector_dimensions[0] / 2, selector_dimensions[1] / 2),
                          selector_dimensions, (self.width / 2 - button_dimensions[0] - 35, self.height / 2 +
                                                self.selection_height), button_dimensions)

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['up']:
            if self.selection_num == 0:
                self.selection_num = 3
            else:
                self.selection_num -= 1

        if key == simplegui.KEY_MAP['down']:
            if self.selection_num == 3:
                self.selection_num = 0
            else:
                self.selection_num += 1

        if key == simplegui.KEY_MAP['space']:
            self.button_selected = True
