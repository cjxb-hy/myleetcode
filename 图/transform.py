from graphmodule import Graph
from nodesmodule import Nodes
from edgesmodule import Edges

"""
matrix = [
    [0,1,5],
    [1,2,4],
    [0,2,6]
]
"""


def matrix2Graph(matrix: list) -> Graph:
    graph = Graph()
    for item in matrix:
        src = item[0]
        dst = item[1]
        weight = item[2]
        if graph.nodes.get(src) is None:
            graph.nodes[src] = Nodes(src)
        if graph.nodes.get(dst) is None:
            graph.nodes[dst] = Nodes(dst)

        srcNode = graph.nodes.get(src)
        dstNode = graph.nodes.get(dst)
        newEdges = Edges(weight, srcNode, dstNode)
        srcNode.nexts.append(dstNode)
        srcNode.outside += 1
        dstNode.inside += 1
        srcNode.edges.append(newEdges)
        graph.edges.add(newEdges)
    return graph
