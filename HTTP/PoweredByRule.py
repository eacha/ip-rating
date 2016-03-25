from HTTP import HTTPRule


class PoweredByRule(HTTPRule.HTTPRule):

    def apply_rule(self, obj, score):
        try:
            obj['x_powered_by']
            score.add_score(50)
        except KeyError:
            score.add_score(100)
