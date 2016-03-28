from HTTP.HTTPRule import HTTPRule


class PoweredByRule(HTTPRule):

    def apply_rule(self, obj, score):
        x_powered_by = obj.get('x_powered_by')

        if x_powered_by:
            score.add_score(50)
        else:
            score.add_score(100)
