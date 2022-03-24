import queue
import select

from transform import matrix2Graph
from graphmodule import Graph
from nodesmodule import Nodes


class UniFind(object):
    def __init__(self, graph: Graph):
        self.setMap = {}
        for node in graph.nodes.values():
            temp = [node]
            self.setMap[node] = temp

    def issameset(self, src: Nodes, dst: Nodes) -> bool:
        sset = self.setMap[src]
        dset = self.setMap[dst]
        return sset == dset

    def union(self, src: Nodes, dst: Nodes):
        sset = self.setMap[src]
        dset = self.setMap[dst]
        for temp in dset:
            if temp not in sset:
                sset.append(temp)
            self.setMap[temp] = sset


def kruskal(graph: Graph) -> list:
    UnionFind = UniFind(graph)
    priorityque = queue.PriorityQueue()
    for edge in graph.edges:
        priorityque.put(edge)
    result = []
    while not priorityque.empty():
        temp = priorityque.get()
        if not UnionFind.issameset(temp.src, temp.dst):
            result.append(temp)
            UnionFind.union(temp.src, temp.dst)
    return result


if __name__ == '__main__':
    matrix = [
        [0, 1, 7],
        [0, 2, 2],
        [0, 3, 10],
        [1, 3, 20],
        [1, 4, 30],
        [2, 3, 4],
        [1, 0, 7],
        [2, 0, 2],
        [3, 0, 10],
        [3, 1, 20],
        [4, 1, 30],
        [3, 2, 4]
    ]
    graph_ = matrix2Graph(matrix)
    print([(i.src.value, i.dst.value) for i in kruskal(graph_)])
