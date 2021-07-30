import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: TreeNode):
    nums = []

    if root:
        inorderTraversalHelper(root, nums)

    return nums


def inorderTraversalHelper(node, nums):
    if node:
        inorderTraversalHelper(node.left, nums)
        nums.append(node.val)
        inorderTraversalHelper(node.right, nums)


def isSymmetricIterativeLong(root: TreeNode):
    level_nodes = []

    if root.left is None and root.right is None:
        return True

    level_nodes.append(root)

    while len(level_nodes) > 0:
        num_nodes_in_level = len(level_nodes)

        while num_nodes_in_level > 0:
            curr_node = level_nodes.pop(0)
            if curr_node:
                level_nodes.append(curr_node.left)
                level_nodes.append(curr_node.right)

            num_nodes_in_level -= 1

        start = 0
        end = len(level_nodes) - 1

        while start <= end:
            if not level_nodes[start] and not level_nodes[end]:
                start += 1
                end -= 1
            elif (not level_nodes[start] or not level_nodes[end]) or (level_nodes[start].val != level_nodes[end].val):
                return False
            else:
                start += 1
                end -= 1

    return True


def isSymmetricIterativeShort(root: TreeNode):
    queue = collections.deque([root, root])

    while queue:
        left_node = queue.popleft()
        right_node = queue.popleft() if len(queue) > 0 else None

        if not left_node and not right_node:
            continue
        elif not left_node or not right_node:
            return False
        elif left_node.val != right_node.val:
            return False

        queue.append(left_node.left)
        queue.append(right_node.right)
        queue.append(left_node.right)
        queue.append(right_node.left)

    return True


def levelOrder(root: TreeNode):
    result = list()
    deque = collections.deque()

    if root:
        deque.append(root)

    while deque:
        num_nodes_in_level = len(deque)
        curr_level_vals = []
        while num_nodes_in_level > 0:
            curr_node = deque.popleft()
            if curr_node:
                curr_level_vals.append(curr_node.val)

            num_nodes_in_level -= 1

            if curr_node.left:
                deque.append(curr_node.left)
            if curr_node.right:
                deque.append(curr_node.right)

        result.append(curr_level_vals)

    return result


def sortedArrayToBST(nums: []):
    root = None

    if nums:
        mid = len(nums) // 2
        left_nums = nums[0:mid]
        right_nums = nums[mid+1:len(nums)]
        root = TreeNode(nums[mid], sortedArrayToBST(left_nums), sortedArrayToBST(right_nums))

    return root


def levelOrderBottomIter(root: TreeNode):
    result = collections.deque()

    if root:
        deque = collections.deque([root])

        while deque:
            num_nodes_in_level = len(deque)
            level_list = []
            for _ in range(num_nodes_in_level):
                curr_node = deque.popleft()
                level_list.append(curr_node.val)

                if curr_node.left:
                    deque.append(curr_node.left)
                if curr_node.right:
                    deque.append(curr_node.right)

            result.appendleft(level_list)

    return result


def levelOrderBottomRec(root: TreeNode):
    result = []

    if root:
        height = getTreeHeight(root)
        result = [[] for _ in range(height)]
        levelOrderBottomHelper(root, 0, result)

    return result


def levelOrderBottomHelper(root, level, result):
    if root:
        if root.left:
            levelOrderBottomHelper(root.left, level + 1, result)
        if root.right:
            levelOrderBottomHelper(root.right, level + 1, result)

        level_list = result[(len(result) - 1) - level]
        level_list.append(root.val)


def getTreeHeight(root: TreeNode, height=0):
    if root:
        left_height = getTreeHeight(root.left, height) + 1
        right_height = getTreeHeight(root.right, height) + 1
        return max(left_height, right_height)

    return height


def hasPathSum(root: TreeNode, targetSum: int):
    if root:
        if not root.left and not root.right:
            if root.val == targetSum:
                return True
            return False
        elif hasPathSumHelper(root.left, targetSum, root.val) or hasPathSumHelper(root.right, targetSum, root.val):
            return True

    return False


def hasPathSumHelper(root, targetSum, currSum):
    if root:
        currSum += root.val
        if not root.left and not root.right:
            if currSum == targetSum:
                return True
            return False
        elif hasPathSumHelper(root.left, targetSum, currSum) or hasPathSumHelper(root.right, targetSum, currSum):
            return True

    return False


def pathSum(root: TreeNode, targetSum: int):
    paths = list()

    if root:
        currPath = []
        pathSumHelper(root, targetSum, 0, currPath, paths)

    return paths


def pathSumHelper(root, targetSum, currSum, currentPath, paths):
    if root:
        currSum += root.val
        currentPath.append(root.val)

        if not root.left and not root.right and currSum == targetSum:
            paths.append(list(currentPath))
        else:
            pathSumHelper(root.left, targetSum, currSum, currentPath, paths)
            pathSumHelper(root.right, targetSum, currSum, currentPath, paths)

        currentPath.pop()


def sumNumbers(root: TreeNode):
    if not root.left and not root.right:
        return root.val

    return sumNumbersHelper(root.left, root.val) + sumNumbersHelper(root.right, root.val)


def sumNumbersHelper(root, currSum):
    if root:
        currSum = currSum * 10 + root.val

        if not root.left and not root.right:
            return currSum

        return sumNumbersHelper(root.left, currSum) + sumNumbersHelper(root.right, currSum)

    return 0


def maxWidthOfBinaryTree(root: TreeNode):
    maxWidth = 1
    nodeLevelList = [(root, 1)]      # each tuple stores the node and the level it's at

    while len(nodeLevelList) > 0:
        firstNodeIndex = nodeLevelList[0][1]
        lastNodeIndex = nodeLevelList[-1][1]
        widthOfCurrLevel = lastNodeIndex - firstNodeIndex + 1

        maxWidth = max(maxWidth, widthOfCurrLevel)
        nextNodeLevelList = []

        for node, index in nodeLevelList:
            if node.left:
                nextNodeLevelList.append((node.left, index * 2))

            if node.right:
                nextNodeLevelList.append((node.right, index * 2 + 1))

        nodeLevelList = nextNodeLevelList

    return maxWidth


def maxWidthDFS(node: TreeNode, level, index, starts):
    if not node:
        return 0

    if level >= len(starts):
        starts.append(index)

    leftResult = maxWidthDFS(node.left, level + 1, index * 2, starts)
    rightResult = maxWidthDFS(node.right, level + 1, index * 2 + 1, starts)
    return max(index + 1 - starts[level], max(leftResult, rightResult))


# print(levelOrder(sortedArrayToBST([-10, -3, 0, 5, 9])))


# print(getTreeHeight(sortedArrayToBST([-10, -3, 0, 5, 9])))


# print(isSymmetricIterativeShort(TreeNode(1,
#                                     TreeNode(2,
#                                              TreeNode(3, None, None), TreeNode(4, None, None)),
#                                     TreeNode(2,
#                                              TreeNode(4, None, None), TreeNode(3, None, None)))))


print(maxWidthOfBinaryTree(TreeNode(1,
                                    TreeNode(3,
                                             TreeNode(5, None, None), TreeNode(3, None, None)),
                                    TreeNode(2,
                                             None, TreeNode(9, None, None)))))