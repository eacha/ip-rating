from HTTP import HTTPRule


class PoweredByRule(HTTPRule.HTTPRule):
    port = '80'
    protocol = 'http'

    def apply_rule(self, obj, score):
        try:
            obj['x_powered_by']
            score.add_score(50)
        except KeyError:
            score.add_score(100)
