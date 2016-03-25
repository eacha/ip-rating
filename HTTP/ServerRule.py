from HTTP import HTTPRule


class ServerRule(HTTPRule.HTTPRule):

    def apply_rule(self, obj, score):
        try:
            obj['server']
            score.add_score(50)
        except KeyError:
            score.add_score(100)
