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

    def update(self, canvas):
        pass

    def compare_new_score(self, new_score):
        is_highscore = True

        self.top_five.append(str(new_score))
        self.top_five.sort(reverse=True)

        if len(self.top_five) > 5:
            low_score = self.top_five.pop(5)
            if low_score == str(new_score):
                is_highscore = False

        return is_highscore

    def add_score(self, new_name, new_score):
        pass


board = ScoreBoard()
print(board.top_five)
print(board.compare_new_score(5))
print(board.top_five)
print(board.compare_new_score(3))
print(board.top_five)
print(board.compare_new_score(2))
print(board.top_five)
print(board.compare_new_score(1))
print(board.top_five)
