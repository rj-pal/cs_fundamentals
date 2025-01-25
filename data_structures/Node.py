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

    # def __eq__(self, other: object) -> bool:
    #     if not isinstance(other, Node):
    #         return NotImplemented
    #     return self.value == other.value

    # def __lt__(self, other: 'Node[T]') -> bool:
    #     return self.value < other.value


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

    def get_size(self):
        return self.size
    
    def find_item(self, node: Node[T]):
        head = self.get_root()
        while head:
            if head.value == node.value:
                print(f"Node Value {node.value} found")
                return head
            else:
                head = head.get_next()
        print("Node not found")
        return None
    
    def remove_item(self, node: Node[T]):
        if (found_node := self.find_item(node)): # assign the node if found
            if not found_node.get_previous():
                self.root = self.root.get_next() 
                self.root.set_previous(None)
            elif not found_node.get_next():
                self.tail = self.tail.get_previous()
                self.tail.set_next(None)
            else:
                found_node.get_next().set_previous(found_node.get_previous())
                found_node.get_next().get_previous().set_next(found_node.get_next())
            print("Node Value removed.")
            
            self.size -= 1
            return True
        else:
            print("Node not found")
            return found_node    
    
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
            print("The linked list is empty.")
        node = self.get_root()
        c = 1
        print(f"Linked List size {self.size}")
        while node:
            print(f"Node {c}: {node.value}")
            node = node.get_next()
            c += 1
# Example Usage
if __name__ == "__main__":
    node1 = Node(5)
    node2 = Node(10)
    node3 = Node(7)
    node4 = Node(15)
    node5 = Node(25)

    myList = LinkedList()
    myList.add_item(node1)
    myList.add_item(node2)
    myList.add_item(node3)
    myList.add_item(node4)
    myList.add_item(node5)
    # myList.find_item(Node(10))
    # myList.find_item(Node(45))

   
    myList.print_linked_list()
    myList.remove_item(Node(25))
    myList.print_linked_list()
    print(myList.tail)

    # print(Node(4).value == Node(4).value)
    # print(Node(4).__str__)
    # print(Node(4).__str__)
    # print(node4.__str__)
    # print(node5.__str__)
#     myList.find_item(Node(7))
#     myList.find_item(Node(15))
#     myList.find_item(Node(23))
