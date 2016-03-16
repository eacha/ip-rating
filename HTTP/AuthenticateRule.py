import Rules


class Authenticate(Rules.Rules):
    port = '80'
    protocol = 'http'

    def apply_rule(self, obj, score):
        try:
            obj[self.port][self.protocol]['get']['headers']['www_authenticate']
            score.partial_scores.add(0)
            score.set_trim(0)
        except KeyError:
            score.partial_scores.add(100)


