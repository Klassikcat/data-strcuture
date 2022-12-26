from typing import *
import logging


class Node(object):
    def __init__(self, item: Any = None, next: ClassVar = None, is_head: bool = False, is_tail: bool = False) -> None:
        self.item = item
        self.next = next
        self.is_head = is_head
        self.is_tail = is_tail

    def __call__(self) -> Any:
        return self.item

    def get_next(self):
        return self.next

    def set_next(self, value) -> ClassVar:
        self.next = value


class LinkedList(object):
    def __init__(self, items: Optional[List[Any]] = None):
        self.tail = Node(is_tail=True)
        self.head = Node(is_head=True, next=self.tail)
        self.length = 0
        if items:
            for idx, item in enumerate(items):
                self.append(item, idx)

    def remove(self, idx: int):
        prev_node = self.get_pointer(idx-1)
        next_node = self.get_pointer(idx+1)
        prev_node.next = next_node
        self.length -= 1

    def append(self, item: Any, idx: int):
        node_new = Node(item)
        prev_node = self.get_pointer(idx-1)
        next_node = prev_node.next
        prev_node.next = node_new
        node_new.set_next(next_node)
        self.length += 1

    def __setitem__(self, idx, value):
        self.get_pointer(idx).item = value

    def __len__(self):
        return self.length

    def get_pointer(self, idx: int):
        current_node = self.head
        for idx in range(idx + 1):
            current_node = current_node.next
        return current_node

    def __getitem__(self, idx: int):
        return self.get_pointer(idx).item

    def __str__(self):
        return str([self.__getitem__(idx) for idx in range(self.length)])

    def __iter__(self):
        current = self.head.next
        while current.is_tail is False:
            yield current.item
            current = current.next


def __main__():
    linked_list = LinkedList()

    linked_list.append('a', 0)
    linked_list.append('b', 1)
    linked_list.append('d', 2)
    linked_list.append('e', 3)
    linked_list.append('f', 4)
    idx_2_init = linked_list[2].item

    linked_list.append('c', 2)

    idx_2_inserted = linked_list[2].item

    linked_list.remove(2)
    idx_2_removed = linked_list[2].item

    logging.info(f"initial item at idx 2: {idx_2_init}\nafter insert item at idx 2: {idx_2_inserted}\nafter remove item at idx 2: {idx_2_removed}")


if __name__ == "__main__":
    __main__()
