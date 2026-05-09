class WordDictionary:

    def __init__(self):
        self.array = []

    def addWord(self, word: str) -> None:
        self.array.append(word)        

    def search(self, word: str) -> bool:
        for w in self.array:
            if len(w) != len(word):
                continue

            i = 0 
            while i < len(word) :
                if w[i] == word[i] or word[i] == ".":
                    i +=1
                else:
                    break
            if i == len(word):
                return True 
        return False



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)