COUNT = [10]


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
        self.balance = 1


class AVLTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, data):
        self.size = self.size + 1
        self.root = self.insert_node(self.root, data)

    def insert_node(self, root, data):
        if not root:
            return Node(data)
        elif data < root.data:
            root.left = self.insert_node(root.left, data)
        elif data > root.data:
            root.right = self.insert_node(root.right, data)
        else:
            self.size = self.size - 1

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and data < root.left.data:
            return self.right_rotate(root)

        if balance < -1 and data > root.right.data:
            return self.left_rotate(root)

        if balance > 1 and data > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and data < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        subtree = y.left
        y.left = z
        z.right = subtree
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        subtree = y.right
        y.right = z
        z.left = subtree
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def delete(self, data):
        self.size = self.size - 1
        self.root = self.delete_node(self.root, data)

    def delete_node(self, root, data):
        if not root:
            self.size = self.size + 1
            return root
        elif data < root.data:
            root.left = self.delete_node(root.left, data)
        elif data > root.data:
            root.right = self.delete_node(root.right, data)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.get_min_value_node(root.right)
            root.data = temp.data
            root.right = self.delete_node(root.right, temp.data)

        if root is None:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        root.balance = self.get_balance(root)

        if root.balance > 1 and root.left.balance >= 0:
            return self.right_rotate(root)
        if root.balance < -1 and root.right.balance <= 0:
            return self.left_rotate(root)
        if root.balance > 1 and root.left.balance < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if root.balance < -1 and root.right.balance > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)

    def pre_order(self):
        return self.pre_order_1(self.root)

    def pre_order_1(self, root):
        if root is None:
            return
        print("{0} ".format(root.data))
        self.pre_order_1(root.left)
        self.pre_order_1(root.right)

    def get_size(self):
        if self.root is None:
            return 0
        return self.size

    def is_avl(self):
        balance = self.root.balance
        return balance == 1 or balance == 0 or balance == -1

    def print_tree(self):
        self.print_2d(self.root, 0)

    def print_2d(self, root, space):
        if root is None:
            return
        space += COUNT[0]
        self.print_2d(root.right, space)
        print()
        for i in range(COUNT[0], space):
            print(end=" ")
        print(root.data)
        self.print_2d(root.left, space)

    def is_balanced(self):
        return self.is_height_balanced(self.root) > -1

    def is_height_balanced(self, root):
        if root is None:
            return 0
        left_height = self.is_height_balanced(root.left)
        if left_height == -1:
            return -1
        right_height = self.is_height_balanced(root.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1


myTree = AVLTree()
nums = [33, 13, 52, 9, 21, 61, 8, 11]
for num in nums:
    myTree.insert(num)
myTree.print_tree()
myTree.delete(13)
print("After Deletion: ")
myTree.print_tree()
