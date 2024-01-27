class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False

        temp = self.root
        while temp is not None:
            if temp.value == value:
                return True
            if value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False

    def __r_contains(self, current_node, value):
        if current_node == None:
            return False

        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    def __r_insert(self, current_node, value):
        if current_node is None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def __delete_node(self, current_node, value):
        # Node not in tree
        if current_node is None:
            return None
        # Traverse tree left and/or right until you encounter None (value not
        # in tree) or you encounter the value you are looking for.
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            # Leaf node (no children)
            if current_node.left is None and current_node.right is None:
                return None
            # No node on left, but node on right
            elif current_node.left is None:
                current_node = current_node.right
            # No node on right, but node on left
            elif current_node.right is None:
                current_node = current_node.left
            # Child node on left and right
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)

        return current_node

    def delete_node(self, value):
        self.root = self.__delete_node(self.root, value)

    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
    
    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.right is not None:
                queue.append(current_node.right)
            if current_node.left is not None:
                queue.append(current_node.left)
        return results

    def dfs_pre_order(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results

    def dfs_post_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)

        traverse(self.root)
        return results

    def dfs_in_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results

foo = BinarySearchTree()

foo.insert(47)
foo.insert(21)
foo.insert(76)
foo.insert(18)
foo.insert(27)
foo.insert(52)
foo.insert(82)

#print(foo.min_value(foo.root))
#print(foo.min_value(foo.root.right))

#print('BST Contains 27:')
#print(foo.r_contains(27))
#
#print('\nBST Contains 17:')
#print(foo.r_contains(17))

#foo.r_insert(2)
#foo.r_insert(1)
#foo.r_insert(3)
#print('Root:', foo.root.value)
#print('Root -> Left:', foo.root.left.value)
#print('Root -> Right:', foo.root.right.value)
#
#foo.delete_node(2)
#
#print('\nRoot:', foo.root.value)
#print('root.left:', foo.root.left.value)
#print('root.right:', foo.root.right)
#
#print(foo.BFS())

print(foo.dfs_pre_order())

print(foo.dfs_post_order())

print(foo.dfs_in_order())