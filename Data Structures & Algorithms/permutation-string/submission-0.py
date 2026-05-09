class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter1 = Counter(s1)
        counter2 = Counter()
        l = 0   
        for r in range(len(s2)):
            counter2[s2[r]] += 1
            print(counter2)
            if r - l + 1 > len(s1):
                counter2[s2[l]] -= 1
                l += 1
            
            if counter2 == counter1:
                return True
        
        return False
            
            
