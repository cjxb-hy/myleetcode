from transform import matrix2Graph
from graphmodule import Graph
import queue


def topologicalSort(graph: Graph) -> list:
    alist = []
    inmap = {}
    zeroqueue = queue.Queue()
    for node in graph.nodes.values():
        inmap[node] = node.inside
        if node.inside == 0:
            zeroqueue.put(node)
    while not zeroqueue.empty():
        temp = zeroqueue.get()
        alist.append(temp.value)
        for cur in temp.nexts:
            inmap[cur] = inmap[cur] - 1
            if inmap[cur] == 0:
                zeroqueue.put(cur)

    return alist


if __name__ == '__main__':
    matrix = [
        [0, 2, 5],
        [1, 2, 5],
        [1, 3, 4],
        [2, 3, 6],
        [2, 4, 5],
        [3, 4, 5],
        [5, 4, 4],
    ]
    graph_ = matrix2Graph(matrix)
    print(topologicalSort(graph_))
