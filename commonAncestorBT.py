'''
236. lowest common ancestor of a binary tree
'''


class TreeNode(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r

def findParent(curr_node, parent, dp_record_parent):
    '''
    function will complete a 1D dynamic programming list to record each node's parent
    '''
    dp_record_parent[curr_node.val] = parent
    if curr_node.left is None and curr_node.right is None:
        return
    elif curr_node.left is None:
        findParent(curr_node.right, curr_node.val, dp_record_parent)
    elif curr_node.right is None:
        findParent(curr_node.left, curr_node.val, dp_record_parent)
    else:
        findParent(curr_node.right, curr_node.val, dp_record_parent)
        findParent(curr_node.left, curr_node.val, dp_record_parent)

def findCommonAncestor(root, p, q, dp_record_parent):
    """
    Find common ancestor by first tracing parents of starting node p and save
    in a list called ancestorP and then create a dict recording all parents
    of q node. Lastly, we find the earlist node of ancestorP that exists in dict
    """
    ancestorP = [p.val]
    ancestorQ = {}
    parent = p.val
    parent2 = q.val
    # first saved all parents of p from nearest to farthest in order
    while dp_record_parent[parent] != root.val:
        ancestorP.append(dp_record_parent[parent])
        parent = dp_record_parent[parent]
    ancestorP.append(root.val)
    # next built the dict for all parents of q
    ancestorQ[q.val] = 1
    while dp_record_parent[parent2] != root.val:
        ancestorQ[dp_record_parent[parent2]] = 1
        parent2 = dp_record_parent[parent2]
    ancestorQ[root.val] = 1
    # return the earliest common ancestor
    for index, ele in list(enumerate(ancestorP)):
        if ele in ancestorQ:
            return ele


if __name__ == "__main__":
    dp_record_parent = [-1] * 10
    root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7),
                                                         TreeNode(4))), TreeNode(1))
    findParent(root, 3, dp_record_parent)
    result = findCommonAncestor(root, TreeNode(7), TreeNode(1), dp_record_parent)
    print(result)