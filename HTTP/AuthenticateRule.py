from HTTP import HTTPRule


class Authenticate(HTTPRule.HTTPRule):

    def apply_rule(self, obj, score):
        www_authenticate = obj.get('www_authenticate')

        if www_authenticate:
            score.add_score(0)
            score.set_capped(0)
        else:
            score.add_score(100)


