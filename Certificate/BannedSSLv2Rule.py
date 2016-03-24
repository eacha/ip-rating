from Certificate import CertificateRule


class BannedSSLv2Rule(CertificateRule.CertificateRule):

    def apply_rule(self, obj, score):
        try:
            if obj['ssl_2_support']:
                score.add_score(0)
                score.set_capped(0)
        except KeyError:
            return
