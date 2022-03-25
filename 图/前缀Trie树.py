# 前缀树Trie

class TrieNode(object):
    def __init__(self, passpath=0, end=0):
        self.passpath = passpath
        self.end = end
        self.nexts = [None for i in range(26)]


class Trie(object):
    def __init__(self):
        self.head = TrieNode()

    def insert(self, string):
        if string is None:
            return
        node = self.head
        node.passpath += 1
        for char in string:
            index = ord(char) - ord('a')
            if node.nexts[index] is None:
                node.nexts[index] = TrieNode()
            node = node.nexts[index]
            node.passpath += 1
        node.end += 1

    def search(self, string) -> int:
        if string is None:
            return 0
        node = self.head
        for char in string:
            index = ord(char) - ord('a')
            if node.nexts[index] is None:
                return 0
            node = node.nexts[index]
        return node.end

    def perfixCount(self, string) -> int:
        if string is None:
            return 0
        node = self.head
        for char in string:
            index = ord(char) - ord('a')
            if node.nexts[index] is None:
                return 0
            node = node.nexts[index]
        return node.passpath

    def delete(self, string):
        if self.search(string) != 0:
            node = self.head
            node.passpath -= 1
            for char in string:
                index = ord(char) - ord('a')
                node.nexts[index].passpath -= 1
                if node.nexts[index].passpath == 0:
                    node.nexts[index] = None
                    return
                node = node.nexts[index]
            node.end -= 1


if __name__ == '__main__':
    trietree = Trie()
    trietree.insert('abcde')
    trietree.insert('abdef')
    trietree.insert('ade')
    trietree.insert('adbc')
    # trietree.delete('abcde')
    print(trietree.search('abcde'))
    print(trietree.perfixCount('ad'))
