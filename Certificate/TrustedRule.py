import Rules


class TrustedRule(Rules.Rules):
    port = '443'
    protocol = 'https'

    def apply_rule(self, obj, score):
        try:
            if obj[self.port][self.protocol]['heartbleed']['heartbleed_vulnerable']:
                score.set_trim(0)
        except KeyError:
            return
