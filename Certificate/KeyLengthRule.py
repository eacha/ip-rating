import operator

from Certificate import CertificateRule


class KeyLengthRule(CertificateRule.CertificateRule):

    KEY_LENGTH = [
        # operation, key_length_rule, points, capped
        (operator.le, 1024, 0, 0),
        (operator.lt, 2048, 50, 50),
        (operator.lt, 4096, 90, 100),
        (operator.ge, 4096, 100, 100),
    ]

    def score_key_length(self, key_length):
        for rule in self.KEY_LENGTH:
            if rule[0](key_length, rule[1]):
                return (rule[2],rule[3])

    def apply_rule(self, obj, score):
        try:
            if obj['chain_rsa_public_key_length']:
                keys = map(int, str(obj['chain_rsa_public_key_length']).split(','))
                min_key = min(keys)
                key_score = self.score_key_length(min_key)

                score.add_score(key_score[0])
                score.set_capped(key_score[1])
        except KeyError:
            return

