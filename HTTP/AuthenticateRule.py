from HTTP import HTTPRule


class Authenticate(HTTPRule.HTTPRule):

    def apply_rule(self, obj, score):
        try:
            obj['www_authenticate']
            score.add_score(0)
            score.set_capped(0)
        except KeyError:
            score.add_score(100)


