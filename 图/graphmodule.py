from nodesmodule import Nodes
from edgesmodule import Edges


class Graph(object):
    def __init__(self):
        self.nodes = {}
        self.edges = set()
