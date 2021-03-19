import re


class ScoreBoard:
    top_five = []

    def __init__(self):
        file = open("HighScoreTable.txt", "r")
        top_five_string = file.read()
        self.top_five = re.split("[&&]", top_five_string)
        file.close()

    def update(self, canvas):
        pass

    def compare_new_score(self, new_score):
        for i in range(1, len(self.top_five), 2):
            if new_score > self.top_five[i]:
                return True
        return False

    def add_score(self, new_name, new_score):
        new_high_scores = ""
        for i in range(1, len(self.top_five), 2):
            if new_score > self.top_five[i]:
                self.top_five[i] = new_score
                self.top_five[i - 1] = new_name
                new_high_scores += new_name + "&&" + str(new_score) + "&&"
            else:
                new_high_scores += self.top_five[i - 1] + "&&" + str(self.top_five[i]) + "&&"
        file = open("HighScoreTable.txt", "w")
        file.write(new_high_scores)
        file.close()


a_board = ScoreBoard()
print(a_board.top_five)