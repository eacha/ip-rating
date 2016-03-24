from Certificate import CertificateRule


class TrustedRule(CertificateRule.CertificateRule):

    def apply_rule(self, obj, score):
        try:
            if obj['trusted']:
                score.add_score(100)
            else:
                score.add_score(0)
                score.set_capped(0)
        except KeyError:
            return
