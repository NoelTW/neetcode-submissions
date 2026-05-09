class Twitter:

    def __init__(self):
        self.follow_map = defaultdict(set)
        self.post_map = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.post_map[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.follow_map[userId].add(userId)        
        heap = []

        for followee in self.follow_map[userId]:
            for time, tweetId in self.post_map[followee]:
                heapq.heappush(heap, (-time, tweetId))
            
        res = []

        for _ in range(min(10, len(heap))):
            res.append(heapq.heappop(heap)[1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.follow_map[followerId].discard(followeeId)
