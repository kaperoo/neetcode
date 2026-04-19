class Node:
    def __init__(self, end=False):
        self.kids = {}
        self.end = end

class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if curr.kids.get(c,None):
                curr = curr.kids[c]
                continue
            curr.kids[c] = Node()
            curr = curr.kids[c]

        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if not curr.kids.get(c,None):
                return False
            curr = curr.kids[c]
        if curr.end:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if not curr.kids.get(c,None):
                return False
            curr = curr.kids[c]
        return True
        