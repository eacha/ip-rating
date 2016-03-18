import Rules


class HeartbleedRule(Rules.Rules):

    def apply_rule(self, obj, score):
        try:
            if obj['heartbleed_vulnerable']:
                score.add_score(0)
                score.set_trim(0)
        except KeyError:
            return
