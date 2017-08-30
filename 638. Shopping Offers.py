class Solution(object):
    def buy(self, bought, p, needs):
        res = [0] * len(bought)
        for i in xrange(len(bought)):
            res[i] = bought[i] + p[i]
        return tuple(res)
        
        
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        dp = {tuple([0] * len(needs)): 0}
        
        # filter stupid special offers
        for p in special:
            offer_price = p[-1]
            retail_price = sum([p[i] * price[i] for i in xrange(len(needs))])
            if offer_price >= retail_price:
                p[0] = None
        special = [p for p in special if p[0] != None]
        
        # sort special offers according to total # of items
        for p in special:
            p.append(sum(p[:-1]))        
        special.sort(key = lambda x: x[-1])
        
        needs_num = sum(needs)
        stack = [tuple([0] * len(needs))]
        
        # use special offer in a BFS way
        # record all status where no more special offers can be used, i.e., leaves
        leaves = []
        while stack:
            new_stack = []
            while stack:
                bought = stack.pop()
                bought_num = sum(bought)
                can_use_offer = 0
                for p in special:
                    if bought_num + p[-1] > needs_num:
                        break
                    new_bought = self.buy(bought, p, needs)
                    if new_bought:
                        if new_bought in dp:
                            dp[new_bought] = min(dp[new_bought], dp[bought] + p[-2])
                            can_use_offer = 1
                        else:
                            for i in xrange(len(new_bought)):
                                if new_bought[i] > needs[i]:
                                    break
                            else:
                                dp[new_bought] = dp[bought] + p[-2]
                                new_stack.append(new_bought)
                                can_use_offer = 1
                if not can_use_offer:
                    leaves.append(bought)
            stack = new_stack
            
        # till now we can't use any more special offers    
        min_price = float('inf')
        for bought in leaves:
            total_price = dp[bought] + sum([(needs[i] - bought[i]) * price[i] for i in xrange(len(needs))])
            min_price = min(min_price, total_price)
        return min_price