class Score(object):
    MAX_SCORE = 100
    MIN_SCORE = 0

    def __init__(self):
        self.capped = self.MAX_SCORE
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

    def set_capped(self, trim):
        if trim < self.capped:
            self.capped = trim

    def trim_score(self, score):
        if score > self.capped:
            return self.capped
        return score

    def pprint(self):
        print len(self.partial_scores)


class Rules(object):
    port = None
    protocol = None

    name = None
