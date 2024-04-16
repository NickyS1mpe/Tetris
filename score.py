class Score:
    def __init__(self):
        self.score_file = 'scores.txt'

    def get_max_score(self):
        with open(self.score_file, 'r') as f:
            lines = f.readlines()
            score = lines[0].strip()

        return score

    def update_score(self, new_score):
        max_score = self.get_max_score()
        if int(max_score) < int(new_score):
            with open('scores.txt', 'w') as f:
                f.write(str(new_score))
