class Node:
    def __init__(self):
        self.children = dict()
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        def dfs(curr, i):
            if i == len(word):
                return curr.word
            if word[i] == ".":
                for child in curr.children.values():
                    res = dfs(child, i + 1)
                    if res:
                        return True
            else:
                if word[i] not in curr.children:
                    return False
                return dfs(curr.children[word[i]], i + 1)
            return False
        
        return dfs(self.root, 0)