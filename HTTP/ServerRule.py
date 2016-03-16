import Rules


class ServerRule(Rules.Rules):
    port = '80'
    protocol = 'http'

    def apply_rule(self, obj, score):
        try:
            obj[self.port][self.protocol]['get']['headers']['server']
            score.partial_scores.add(60)
        except KeyError:
            score.partial_scores.add(100)
