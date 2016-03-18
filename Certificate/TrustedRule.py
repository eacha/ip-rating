import Rules


class TrustedRule(Rules.Rules):

    def apply_rule(self, obj, score):
        try:
            if obj['trusted']:
                score.add_score(100)
            else:
                score.add_score(75)
                score.set_trim(75)
        except KeyError:
            score.add_score(0)