class Score(object):
    MAX_SCORE = 100
    MIN_SCORE = 0
    FINAL_SCORE = MIN_SCORE

    def __init__(self):
        self.trim = self.MAX_SCORE
        self.partial_scores = list()

    def add_score(self, score):
        self.partial_scores.add(score)

    def calc_avg(self):
        if len(self.partial_scores) == 0:
            return

        for score in self.partial_scores:
            self.FINAL_SCORE += score

        self.FINAL_SCORE /= len(self.partial_scores)
        self.trim_score()

    def set_trim(self, trim):
        if trim < self.trim:
            self.trim = trim

    def trim_score(self):
        if self.FINAL_SCORE > self.trim:
            self.FINAL_SCORE = self.trim


class Rules(object):
    port = None
    protocol = None

    name = None

    def check_open_port(self, obj):
        try:
            obj[self.port]
        except KeyError:
            return False

        return True

