import Rules


class BannedSSLv3Rule(Rules.Rules):

    def apply_rule(self, obj, score):
        try:
            if obj['ssl_3']:
                score.set_trim(0)
        except KeyError:
            return
