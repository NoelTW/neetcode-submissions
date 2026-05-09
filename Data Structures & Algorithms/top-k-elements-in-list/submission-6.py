class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for num in nums:
            counter[num] = counter.get(num,0) + 1
        

        freqs = sorted( [(num, freq) for num, freq in counter.items()], key= lambda x: x[1], reverse=True)
        return [num for num, freq in freqs[:k]]
            
