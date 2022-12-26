from typing import *
from .queue import Queue

class BinaryTreeNode(object):
    def __init__(self, value: Union[int, float], parent: object) -> None:
        self.parent = parent
        self.value = value
        self.left = None
        self.right = None

    def set_child(self, node):
        if self.value < node.value:
            self.right = node
        elif self.value > node.value:
            self.left = node
        else:
            pass

    def __call__(self) -> Any:
        return self.item

    def get_next(self):
        return self.next

    def set_next(self, value) -> ClassVar:
        self.next = value


class BinarySearchTree(object):
    def __init__(self, tree_values: Optional[Union[int, float]] = None):
        self.root = None
        if tree_values:
            for i in tree_values:
                self.insert(i)

    def insert(self, value: Union[float, int], node: None = None):
        if node is None:
            node = self.root

        if self.root is None:
            self.root = BinaryTreeNode(value)
            return None
        if node.value < value:
            if node.left != None:
                return self.insert(value, node.left)
        elif node.value > value:
            if node.right != None:
                return self.insert(value, node.right)
        elif node.value == value:
            return None
        else:
            node_to_insert = BinaryTreeNode(value, node)
            node.set_child(node_to_insert)
        return None

    def delete(self, value: Union[float, int], node: object = None):
        if node is None:
            node = self.root

        if node.value > value:
            return self.delete(value, node.left)
        elif node.value < value:
            return self.delete(value, node.right)
        elif node.value == value:
            parent = node.parent

        if node.left is None and node.right is None:
            if parent.value > node.value:
                parent.left = None
            else:
                parent.right = None
        else:
            if node.left and node.right:
                next_node = node.left
                new_node_val = self.max(next_node).value
                node = BinaryTreeNode(new_node_val)
            else:
                child_node = node.left if node.left is not None else node.right
                if node.left:
                    parent.left = child_node
                else:
                    parent.right = child_node

    def search(self, value: Union[float, int], node: object = None):
        if node is None:
            node = self.root
        if value == node.value:
            return True
        elif value < node.value:
            left_node = node.left
            if left_node is None:
                return False
            else:
                return self.search(value, left_node)
        elif value > node.value:
            right_node = node.right
            if right_node is None:
                return False
            else:
                return self.search(value, right_node)

    def max(self, node: object = None):
        if node is None:
            node = self.root
        if node.right is None:
            return node
        else:
            return self.max(node.right)

    def min(self, node: object = None):
        if node is None:
            node = self.root
        if node.left is None:
            return node
        else:
            return self.min(node.left)

    def depth_first_traverse(self, order: str = 'sequential', node: object = None):
        if node is None:
            node = self.root
        ret = []
        if order == 'sequential':
            ret.append(node.value)
        if node.left is not None:
            ret = ret + self.depth_first_traverse(order, node.left)
        if order == 'sorted':
            ret.append(node.value)
        if node.right is not None:
            ret = ret + self.depth_first_traverse(order, node.right)
        if order == 'inverse':
            ret.append(node.value)
        return ret

    def level_order_traverse(self, node: object = None):
        ret = []
        queue = Queue()
        queue.enqueue(self.root)
        while len(queue) > 0:
            node = queue.dequeue()
            if node is None:
                continue
            ret.append(node.value)
            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.dequeue(node.right)
        return ret

    def __itr__(self):
        return self.depth_first_traverse(order='sorted')

    def __str__(self):
        return str(self.__itr__())