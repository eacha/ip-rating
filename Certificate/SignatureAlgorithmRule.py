from Certificate import CertificateRule


class SignatureAlgorithmRule(CertificateRule.CertificateRule):

    HASH_ALGORITHM = [
        ('MD2', (0, 0)),
        ('MD5', (0, 0)),
        ('SHA1', (50, 50)),
        ('SHA224', (100, 100)),
        ('SHA256', (100, 100)),
        ('SHA384', (100, 100)),
        ('SHA512', (100, 100)),
    ]

    def update_score(self, old_score, new_score):
        if old_score[0] > new_score[0]:
            return new_score
        return old_score

    def score_min_hash_algorithm(self, chain_signature):
        score = (100, 100)
        for sign in chain_signature:
            for hash_algorithm in self.HASH_ALGORITHM:
                if hash_algorithm[0] in sign:
                    score = self.update_score(score, hash_algorithm[1])
                    break
            else:
                score = (0, 0)
        return score

    def apply_rule(self, obj, score):
        raw_chain_signature = obj.get('chain_signature_algorithm')

        if raw_chain_signature is None:
            return

        chain_signature = str(raw_chain_signature).split(',')
        hash_score = self.score_min_hash_algorithm(chain_signature)

        score.add_score(hash_score[0])
        score.set_capped(hash_score[1])