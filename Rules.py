class Score(object):
    MAX_SCORE = 100
    MIN_SCORE = 0

    def __init__(self):
        self.trim = self.MAX_SCORE
        self.partial_scores = list()

    def add_score(self, score):
        self.partial_scores.append(score)

    def calc_avg(self):
        if len(self.partial_scores) == 0:
            return None

        final_score = 0
        for score in self.partial_scores:
            final_score += score

        final_score /= float(len(self.partial_scores))
        return self.trim_score(final_score)

    def set_trim(self, trim):
        if trim < self.trim:
            self.trim = trim

    def trim_score(self, score):
        if score > self.trim:
            return self.trim
        return score

    def pprint(self):
        print len(self.partial_scores)


class Rules(object):
    port = None
    protocol = None

    name = None
