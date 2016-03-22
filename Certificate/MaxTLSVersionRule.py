from Certificate import CertificateRule


class MaxTLSVersionRule(CertificateRule.CertificateRule):

    # version name -> (score, trim)
    TLS_VERSION = {
        'TLSv1.2': (100, 100),
        'TLSv1.1': (90, 90),
        'TLSv1.0': (50, 50),
        'SSLv3.0': (0, 0),
        'SSLv2.0': (0, 0)
    }

    def apply_rule(self, obj, score):
        try:
            version = obj['tls_version']
            score.add_score(self.TLS_VERSION[version][0])
            score.set_trim(self.TLS_VERSION[version][1])
        except KeyError:
            return
