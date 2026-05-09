class MinHeap:
    
    def __init__(self):
        self.heap = [-1]

    def push(self, val: int) -> None:
        self.heap.append(val)
        i = len(self.heap) - 1
        while self.heap[i] < self.heap[i//2] and i//2 != 0 :
            self.heap[i], self.heap[i // 2] = self.heap[i//2], self.heap[i]
            i //= 2


    def pop(self) -> int:
        if len(self.heap) == 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()
        res = self.heap[1]  
        # make sure well constructed
        self.heap[1] = self.heap.pop()
        # Percolate down
        i = 1
        self.percolate_down(i)
        return res

        

    def top(self) -> int:
        return self.heap[1] if len(self.heap) > 1 else -1


    def heapify(self, nums: List[int]) -> None:
        self.heap = [-1] + nums 
        cur = (len(self.heap) -1) //2
        while cur > 0:
            i = cur
            self.percolate_down(i)
            cur -=1

    # Percolate down
    def percolate_down(self, i):
        while 2 * i < len(self.heap):
            if (2 * i + 1 < len(self.heap) and 
            self.heap[2 * i + 1] < self.heap[2 * i] and 
            self.heap[i] > self.heap[2 * i + 1]):
                # Swap right child
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i + 1]
                self.heap[2 * i + 1] = tmp
                i = 2 * i + 1
            elif self.heap[i] > self.heap[2 * i]:
                # Swap left child
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i]
                self.heap[2 * i] = tmp
                i = 2 * i
            else:
                break



        
        