class Node:
    def __init__(self, end=False):
        self.kids = {}
        self.end = end

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if curr.kids.get(c,None):
                curr = curr.kids[c]
                continue
            curr.kids[c] = Node()
            curr = curr.kids[c]
        curr.end = True
        

    def search(self, word: str) -> bool:
        return any(self.dot(self.root,word))

    def dot(self, node, word):

        for i,c in enumerate(word):

            if c == '.':
                opt = [False]
                for k in node.kids:
                    opt.extend(self.dot(node.kids[k],word[i+1:]))
                return opt

            if not node.kids.get(c,None):
                return [False]            
            node = node.kids[c]

        return [node.end]
