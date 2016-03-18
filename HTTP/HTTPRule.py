import Rules


class HTTPRule(Rules.Rules):

    def __init__(self):
        super(HTTPRule, self).__init__()

    @classmethod
    def all_subclasses(cls):
        return cls.__subclasses__() + [g for s in cls.__subclasses__()
                                       for g in s.all_subclasses()]