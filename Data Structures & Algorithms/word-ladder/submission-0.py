class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        word_map = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                word_map[pattern].append(word)
        
        # BFS
        q = deque([beginWord])
        visit = set([beginWord])
        res =  1
        while q:
            print(q)
            for word in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for nei in word_map[pattern]:
                        if nei not in visit:
                            q.append(nei)
                            visit.add(nei)
            res += 1
        
        return 0