
class TrieNode(object):
    def __init__(self):
        self.children = dict()
        self.word = None

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word:str):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = word
    


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        n, m = len(board), len(board[0])

        def dfs(r, c, node):
            if node.word:
                ans.append(node.word)
                node.word=None

            temp = board[r][c]
            board[r][c] = "#"
            for dr, dc in [(0,1), (1,0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and board[nr][nc] in node.children:
                    dfs(nr, nc, node.children[board[nr][nc]])
            board[r][c] = temp
            
            
        for word in words:
            trie.insert(word)
        
        ans = []
        for r in range(n):
            for c in range(m):
                if board[r][c] in trie.root.children:
                    dfs(r,c, trie.root.children[board[r][c]])
        
        return ans
                    
            