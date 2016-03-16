import Rules


class TrustedRule(Rules.Rules):
    port = '443'
    protocol = 'https'

    def apply_rule(self, obj, score):
        try:
            if obj[self.port][self.protocol]['tls']['validation']['browser_trusted']:
                score.add_score(100)
            else:
                score.add_score(75)
                score.set_trim(75)
        except KeyError:
            return
