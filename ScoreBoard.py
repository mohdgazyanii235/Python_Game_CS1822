import re


class ScoreBoard:
    top_five = []

    def __init__(self):
        file = open("HighScoreTable.txt", "r")
        item = file.readline()

        while item:
            item = item[0:len(item) - 1]
            # Removes the /n
            self.top_five.append(item)
            item = file.readline()

        file.close()

        for x in range(0, 10 - len(self.top_five)):
            self.top_five.append("--")

    def update(self, canvas):
        pass

    def compare_new_score(self, new_score):
        pass

    def add_score(self, new_name, new_score):
        pass


board = ScoreBoard()
print(board.top_five)