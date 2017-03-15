import Queue

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def search(node, depth):
    if node.left == None and node.right == None:
    	return (node.val, depth)
    (l_val, l_depth) = (0, 0)
    (r_val, r_depth) = (0, 0)
    if node.left != None:
    	(l_val, l_depth) = search(node.left, depth + 1)
    if node.right != None:
    	(r_val, r_depth) = search(node.right, depth + 1)
    if l_depth < r_depth:
    	return (r_val, r_depth)
    else:
        return (l_val, l_depth)

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #This solution is to deal with the input form like [2, 1, 3]. The idea is to build a tree first and then travel the tree recursively.
        q = Queue.Queue()
        r = TreeNode(root[0])
        q.put(r)
        count = 0
        while (not q.empty()) and count < len(root):
        	node = q.get()
        	if count + 1 < len(root) and root[count + 1] != None:
        		node.left = TreeNode(root[count + 1])
        		q.put(node.left)
        	if count + 2 < len(root) and root[count + 2] != None:
        		node.right = TreeNode(root[count + 2])
        		q.put(node.right)
        	count += 2
        (val, depth) = search(r, 0)
        return val

class Solution_2(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #This solution is to deal with the input tree which has been built.
        (val, depth) = search(root, 0)
        return val

class Solution_3(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #Idea: right-to-left BFS means the last node will be BottomLeftValue!
        q = [root]
        for node in q:
        	q += filter(None, [node.right, node.left])
        return node.val

s = Solution()
print s.findBottomLeftValue([1,None,2,3])
        
