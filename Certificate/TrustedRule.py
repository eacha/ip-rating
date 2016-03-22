from Certificate import CertificateRule


class TrustedRule(CertificateRule.CertificateRule):

    def apply_rule(self, obj, score):
        try:
            if obj['trusted']:
                score.add_score(100)
            else:
                score.add_score(75)
                score.set_trim(75)
        except KeyError:
            return
