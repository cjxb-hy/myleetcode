from transform import matrix2Graph
from nodesmodule import Nodes
import queue


def widthsearch(node: Nodes) -> list:
    if node is None:
        return []
    alist = []
    nodeque = queue.Queue()
    nodeset = set()
    nodeque.put(node)
    nodeset.add(node)
    while not nodeque.empty():
        temp = nodeque.get()
        alist.append(temp.value)
        for cur in temp.nexts:
            if cur not in nodeset:
                nodeset.add(cur)
                nodeque.put(cur)
    return alist


if __name__ == '__main__':
    matrix = [
        [0, 1, 5],
        [0, 3, 5],
        [1, 4, 4],
        [2, 4, 6],
        [1, 0, 5],
        [3, 0, 5],
        [4, 1, 4],
        [4, 2, 6],
    ]
    graph = matrix2Graph(matrix)
    print(widthsearch(graph.nodes[0]))

