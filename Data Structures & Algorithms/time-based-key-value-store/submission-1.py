class TimeMap:

    def __init__(self):

        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        array = self.store[key]
        l , r = 0, len(array) 
        best_index = -1 
        while l < r:
            m = l + (r - l) // 2
            m_timestamp = array[m][0]
            if m_timestamp <= timestamp:
                best_index = m
                l = m + 1
            else:
                r = m
        return array[best_index][1] if best_index != -1 else ""
