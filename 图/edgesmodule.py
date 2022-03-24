from nodesmodule import Nodes


class Edges(object):
    def __init__(self, weight: int, src: Nodes, dst: Nodes):
        self.weight = weight
        self.src = src
        self.dst = dst

    def __lt__(self, other):
        return self.weight < other.weight
