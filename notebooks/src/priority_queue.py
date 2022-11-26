
from typing import *


class Node(object):
    def __init__(self, item: Any = None, priority: int = 0, next: ClassVar = None, prev: ClassVar = None, is_head: bool = False, is_tail: bool = False) -> None:
        self.item = item
        self.next = next
        self.prev = prev
        self.is_head = is_head
        self.is_tail = is_tail
        self.priority = priority

    def __call__(self) -> Any:
        return self.item

    def get_next(self) -> ClassVar:
        return self.next

    def get_prev(self) -> ClassVar:
        return self.prev

    def set_next(self, value: ClassVar) -> None:
        self.next = value

    def set_prev(self, value: ClassVar) -> None:
        self.prev = value


class LinkedList(object):
    def __init__(self, items: Optional[List[Any]] = None):
        self.tail = Node(is_tail=True)
        self.head = Node(is_head=True, next=self.tail)
        self.length = 0
        if items:
            for idx, item in enumerate(items):
                self.append(item, idx)

    def remove(self, idx: int):
        prev_node = self[idx-1]
        next_node = self[idx+1]
        prev_node.next = next_node
        self.length -= 1

    def append(self, item: Any, idx: int, priority: int = 0):
        node_new = Node(item, priority)
        self._insert(node_new, idx)

    def _insert(self, node, idx):
        prev_node = self[idx-1]
        next_node = prev_node.next
        prev_node.next = node
        node.set_next(next_node)
        self.length += 1

    def __len__(self):
        return self.length

    def __getitem__(self, idx):
        current_node = self.head
        for _ in range(idx + 1):
            current_node = current_node.next
        return current_node

    def __itr__(self):
        current_node = self.head.next
        while current_node.is_tail is False:
            yield current_node
            current_node = current_node.next

    def __setitem__(self, index, value):
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        self.remove(index)
        self._insert(value, index)


class PriorityQueue(object):
    def __init__(self, items: Optional[List[Any]] = None, mode: str = 'lazy'):
        self.items = LinkedList(items)
        self.mode = mode

    def enqueue(self, item: Any, priority: int = 0):
        self.items.append(item, 0, priority)
        if self.mode == 'earlybird':
            self._sort()

    def _sort(self):
        for idx in range(len(self.items) - 1):
            if self.items[idx].is_tail:
                break
            if self.items[idx].priority > self.items[idx+1].priority:
                self.items[idx], self.items[idx+1] = self.items[idx+1], self.items[idx]

    def dequeue(self):
        if self.mode == 'lazy':
            self._sort()
        self.items.remove(self.__len__() - 1)

    def __len__(self):
        return len(self.items)

    def __itr__(self):
        for i in range(len(self) - 1):
            yield self[i]

    def __str__(self):
        return str([i for i in self])

    def __getitem__(self, idx):
        if idx >= len(self):
            raise IndexError("Index out of range")
        return self.items[idx].item

    def max(self):
        max_value = 0
        for i in self:
            if i.priority > max_value:
                max_value = i.priority
        return max_value

    def min(self):
        min_value = self[0].priority
        for i in self:
            if i.priority < min_value:
                min_value = i.priority
        return min_value


