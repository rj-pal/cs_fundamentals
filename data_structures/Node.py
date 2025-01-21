from typing import Generic, TypeVar, Optional

T = TypeVar('T')

class Node(Generic[T]):
    """
    A base class for a Node object.

    This class handles generic behavior for a Node object that can be used to 
    implement Linked Lists, Ques or Stacks that follows basic conventions of 
    setters and getters.
    """

    def __init__(self, value: T):
        self.value: T = value
        self.next: Optional['Node[T]'] = None
        self.previous: Optional['Node[T]'] = None

    def set_next(self, node: Optional['Node[T]']) -> Optional['Node[T]']:
        """Set the next node."""
        self.next = node
        return self.next 

    def set_previous(self, node: Optional['Node[T]']) -> Optional['Node[T]']:
        """Set the previous node."""
        self.previous = node
        return self.previous

    def get_next(self) -> Optional['Node[T]']:
        """Get the next node."""
        return self.next #if self.next else 'None'

    def get_previous(self) -> Optional['Node[T]']:
        """Get the previous node."""
        return self.previous #if self.previous else 'None'
    
    # def compare_to(self, node: Optional['Node[T]']) -> int:
    #     """Compare this node's value to another node's value."""
    #     if node is None:
    #         return -1
    #     if self.value < node.value:
    #         return -1
    #     elif self.value > node.value:
    #         return 1
    #     else:
    #         return 0
    

    def __str__(self):
        """Return a string representation of the node."""
        return f"Node({self.value})"

class LinkedList():

    def __init__(self):
        self.root: Optional['Node[T]'] = None
        self.tail: Optional['Node[T]'] = None
        self.size: int = 0

    def get_root(self):
        return self.root
    
    def add_item(self, node: Node[T]):
        if not self.root:
            self.root = node
            self.tail = node
            self.size += 1
            return True
        else:
            self.tail.set_next(node)
            node.set_previous(self.tail)
            self.tail = node
            self.size += 1
            return True
    
    def print_linked_list(self) -> None:
        if not self.root:
            return "The linked list is empty."
        linkedlist = ''
        node = self.get_root()
        c = 1
        while node:
            linkedlist += f"Node {c}: {node.value}\n"
            node = node.get_next()
            c += 1
        print(linkedlist)

# Example Usage
if __name__ == "__main__":
    node1 = Node(5)
    node2 = Node(10)
    node3 = Node(7)

    myList = LinkedList()
    myList.add_item(node1)
    myList.add_item(node2)
    myList.add_item(node3)

    # # Print nodes
    print(node1.value)  # Output: Node(5)
    print(node1.get_next().value)  # Output: Node(10)
    print(node2.get_previous().value)  # Output: Node(5)
    # print(node3.get_next().value)
    myList.print_linked_list()
