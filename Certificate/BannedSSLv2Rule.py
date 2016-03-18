import Rules


# class BannedSSLv2Rule(Rules.Rules):
#     port = '443'
#     protocol = 'https'
#
#     def apply_rule(self, obj, score):
#         try:
#             if obj[self.port][self.protocol]['ssl_2']['support']:
#                 score.set_trim(0)
#         except KeyError:
#             return
