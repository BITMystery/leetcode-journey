import heapq


class Twitter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = 0
        self.tweets = {}
        self.follows = {}

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
        Retrieve the 10 most recent tweet ids in the user's news feed. Each
        item in the news feed must be posted by users who the user followed or
        by the user herself. Tweets must be ordered from most recent to least
        recent.
        :type userId: int
        :rtype: List[int]
        """
        users = list(self.follows.get(userId, set()) | set([userId]))
        pointers = [len(self.tweets.get(u, [])) - 1 for u in users]
        h = []
        heapq.heapify(h)
        for i in xrange(len(users)):
            if pointers[i] >= 0:
                heapq.heappush(h, self.tweets[users[i]][pointers[i]] + [i])
                pointers[i] -= 1
        feed = []
        while h and len(feed) < 10:
            time, tweet, i = heapq.heappop(h)
            feed.append(tweet)
            if pointers[i] >= 0:
                heapq.heappush(h, self.tweets[users[i]][pointers[i]] + [i])
                pointers[i] -= 1
        return feed

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be
        a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.follows:
            self.follows[followerId].add(followeeId)
        else:
            self.follows[followerId] = set([followeeId])

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should
        be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.follows:
            if followeeId in self.follows[followerId]:
                self.follows[followerId].remove(followeeId)
