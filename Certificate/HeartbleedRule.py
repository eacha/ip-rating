from Certificate import CertificateRule


class HeartbleedRule(CertificateRule.CertificateRule):

    def apply_rule(self, obj, score):
        try:
            if obj['heartbleed_vulnerable']:
                score.add_score(0)
                score.set_capped(0)
            else:
                score.add_score(100)
        except KeyError:
            # Heartbeat disable
            score.add_score(100)
