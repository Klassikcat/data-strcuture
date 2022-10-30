# Data Strcuture in Python

## Introduction

This is a collection of data structures in Python. The data structures are implemented in Python 3.9, but you can
implement this unless you're using python 2.*. 

The data structures are:
1. Linked List
2. Stack
3. Queue
4. Memoization
5. Tree
6. Graph
7. Binary Search Tree
8. Etc...

## How to use

To learn about structure, you can see notebooks to get detailed explanation. If you want to use the data structure, you can
import the data structure from the file. For example, if you want to use linked list, you can import it like this:

```python
from src.linked_list import LinkedList

linked_list = LinkedList([1, 2, 3])
linked_list.append(4, 3)
linked_list.remove(2)

print(linked_list)
> [1, 2, 4]
```

Note that you can't use the data structures exactly same as a list, for __getitem__ method returns reference(pointer) 
address of the node. If you want to get the value of the node, you can use `linked_list_instance[idx].item`.