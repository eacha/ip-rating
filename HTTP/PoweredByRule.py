import Rules


class PoweredByRule(Rules.Rules):
    port = '80'
    protocol = 'http'

    def apply_rule(self, obj, score):
        try:
            obj[self.port][self.http]['get']['headers']['x_powered_by']
        except KeyError:
            score.partial_scores.add(100)

        score.partial_scores.add(60)
