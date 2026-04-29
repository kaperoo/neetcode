class Twitter:

    def __init__(self):
        self.tweets = []
        heapq.heapify(self.tweets)
        self.follows = {}
        self.idx = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.tweets,(-self.idx,tweetId,userId))
        self.idx += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = self.tweets.copy()
        res = []
        while heap:
            tweet = heapq.heappop(heap)
            uid = tweet[2]
            if uid in self.follows.get(userId,set()) or uid == userId:
                res.append(tweet[1])
            
            if len(res) == 10:
                break
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId] = self.follows.get(followerId,set())
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        
