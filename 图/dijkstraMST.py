import queue
import select
import sys

from transform import matrix2Graph
from graphmodule import Graph
from nodesmodule import Nodes


def dijkstra(head: Nodes) -> dict:
    # 从head出发到所有节点的最小距离
    # key: 从head出发到节点key
    # value: 从head出发到key的最小距离
    distanceMap = {head: 0}
    selectedNodes = set()
    minNode = getMinDistanceNode(distanceMap, selectedNodes)
    while minNode is not None:
        mindistance = distanceMap[minNode]
        for edge in minNode.edges:
            dstNode = edge.dst
            if dstNode not in distanceMap.keys():
                distanceMap[dstNode] = mindistance + edge.weight
            distanceMap[dstNode] = min(distanceMap[dstNode], mindistance + edge.weight)
        selectedNodes.add(minNode)
        minNode = getMinDistanceNode(distanceMap, selectedNodes)
    return distanceMap


def getMinDistanceNode(distanceMap, selectedNodes):
    mindistance = sys.maxsize
    node = None
    for temp in distanceMap.keys():
        if temp not in selectedNodes and distanceMap[temp] < mindistance:
            mindistance = distanceMap[temp]
            node = temp
    return node


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
    dmap = dijkstra(graph_.nodes[0])
    print([(i.value, dmap[i]) for i in dmap.keys()])
