from HTTP.HTTPRule import HTTPRule


class ServerRule(HTTPRule):

    def apply_rule(self, obj, score):
        server = obj.get('server')

        if server:
            score.add_score(50)
        else:
            score.add_score(100)
