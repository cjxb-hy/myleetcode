class Nodes(object):
    def __init__(self, value: int):
        self.value = value
        self.inside = 0
        self.outside = 0
        self.nexts = []
        self.edges = []
