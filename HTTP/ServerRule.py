import Rules


class ServerRule(Rules.Rules):
    port = '80'
    protocol = 'http'

    def apply_rule(self, obj, score):
        try:
            obj[self.port][self.protocol]['get']['headers']['server']
        except KeyError:
            score.partial_scores.add(100)

        score.partial_scores.add(60)
