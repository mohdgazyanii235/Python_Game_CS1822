class ScoreBoard:
    top_five = []

    def __init__(self):
        file = open("HighScoreTable.txt", "r")
        item = file.readline()

        while item:
            item = item[0:len(item) - 1]
            # Removes the /n
            self.top_five.append(int(item))
            item = file.readline()

        file.close()

    def compare_new_score(self, new_score):
        is_highscore = True

        self.top_five.append(int(new_score))
        self.top_five.sort(reverse=True)

        if len(self.top_five) > 5:
            low_score = self.top_five.pop(5)
            if low_score == new_score:
                is_highscore = False

        self.top_five.sort(reverse=True)

        if is_highscore:
            file = open("HighScoreTable.txt", "w")
            for x in self.top_five:
                file.writelines(str(x) + "\n")

        return is_highscore



