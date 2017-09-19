import heapq

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = 0
        self.tweets = {}
        self.follow_index = {}
        

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId in self.tweets:
            self.tweets[userId].append([-self.time, tweetId])
        else:
            self.tweets[userId] = [[-self.time, tweetId]]
        self.time += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        res = []
        s = self.follow_index.get(userId, set())
        s.add(userId)
        users = list(s)
        pointers = [len(self.tweets.get(users[i], [])) - 1 for i in xrange(len(users))]
        h = []
        heapq.heapify(h)
        for i in xrange(len(users)):
            if pointers[i] >= 0:
                heapq.heappush(h, self.tweets[users[i]][pointers[i]] + [i])
        while len(res) < 10 and h:
            [time, tweet, i] = heapq.heappop(h)
            res.append(tweet)
            pointers[i] -= 1
            if pointers[i] >= 0:
                heapq.heappush(h, self.tweets[users[i]][pointers[i]] + [i])
        return res
        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.follow_index:
            self.follow_index[followerId].add(followeeId)
        else:
            self.follow_index[followerId] = set([followeeId])
        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.follow_index:
            if followeeId in self.follow_index[followerId]:
                self.follow_index[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)