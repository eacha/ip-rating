from Certificate import CertificateRule


class BannedSSLv3Rule(CertificateRule.CertificateRule):

    def apply_rule(self, obj, score):
        try:
            if obj['ssl_3']:
                score.set_trim(0)
        except KeyError:
            return
