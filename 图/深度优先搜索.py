from transform import matrix2Graph
from nodesmodule import Nodes


def depthsearch(node: Nodes) -> list:
    if node is None:
        return []
    alist = []
    nodestack = []
    nodeset = set()
    nodestack.append(node)
    nodeset.add(node)
    alist.append(node.value)
    while len(nodestack) > 0:
        temp = nodestack.pop()
        for cur in temp.nexts:
            if cur not in nodeset:
                nodestack.append(temp)
                nodestack.append(cur)
                nodeset.add(cur)
                alist.append(cur.value)
                break
    return alist


if __name__ == '__main__':
    matrix = [
        [0, 1, 5],
        [0, 2, 5],
        [0, 3, 5],
        [1, 4, 4],
        [2, 4, 6],
        [1, 0, 5],
        [2, 0, 5],
        [3, 0, 5],
        [4, 1, 4],
        [4, 2, 6],
    ]
    graph = matrix2Graph(matrix)
    print(depthsearch(graph.nodes[0]))
