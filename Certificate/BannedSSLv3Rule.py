from Certificate import CertificateRule


class BannedSSLv3Rule(CertificateRule.CertificateRule):

    def apply_rule(self, obj, score):
        try:
            if obj['ssl_3_support']:
                score.set_capped(50)
        except KeyError:
            return
