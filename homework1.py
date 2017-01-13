# Use this class to implement the Stack
# A stack is a data structure from which items can be added and removed.
# Just like a stack of books, plates, lunch trays, or anything else, items are both removed from, and added to, the "top" of the stack.
class Stack:
    def __init__(self):
        self.items = []

    # Use this function to insert a new element in the Stack
    # None should never be able to be pushed into a stack.
    def push(self, item):
        if item is not None:
            self.items.append(item)
        else:
            print('None should never be able to be pushed into a stack')
    
    # Use this function to remove and return the top element from the Stack
    # The item popped from a stack is always the last item added (pushed) to the stack.
    # If no items are present in the stack, pop() returns None.
    def pop(self):
        if self.items == []:
            return None
        else:
            return self.items.pop()

    # Use this function to read the top element in the Stack without removing it.
    # This function returns the same value as pop(), but does not change the stack.
    # Repeated, consecutive calls to peek() will always return the same value.
    def peek(self):
        return self.items[len(self.items)-1]

# Use this class to implement the FIFO (First In First Out) Queue
# A FIFO Queue is a data structure where the first item added to the data structure is the first item removed.
# A queue acts like a line at the movies - the first person to line up is the first person into the theatre.
class Queue:
    def __init__(self):
        self.items = []
        
    # Use this function to insert a new element in the Queue
    # None should never be able to be inserted into the Queue.
    def enqueue(self, item):
        if items is not None:
            self.items.insert(0, item)
        else:
            print('None should never be able to be inserted into the Queue.')

    # Use this function to remove and return the next element from the Queue
    # If the Queue is empty, this function should return None
    def dequeue(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items.pop(0)
    
    # Use this function to read the top element in the Queue without removing it
    # This function returns the same value as dequeue(), but does not change the stack.
    # Repeated, consecutive calls to peek() will always return the same value.
    def peek(self):
        return self.items[0]

# Use this class to implement the LinkedList
# A Linked List is a data structure made of Nodes, which each contain a reference to the next Node in the list
# You may choose to construct a Doubly Linked List, where each Node also contains a reference to the previous Node in the list, but doing so is not required.
# The important idea is that Nodes don't know about all of the items in the list, only the next (and in a Doubly Linked List, the previous) element.
# You should not have a table of all of the elements in this structure.
class LinkedList:
    def __init__(self):
        self.head = None

    # Use this function to insert a new element in the LinkedList
    # Like a stack, elements should be added to the front (called the head) of the LinkedList.
    # None should not be allowed to be added to the list.
    def insert(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            node.next.prev = node
            self.head = node

    # Use this function to find a Node with the specified data in the LinkedList
    # If the end of the list is reached, and the data are not found, return None.
    # If the list contains multiple Nodes with the requested Data, you only need to return the first one you find.
    def find(self, data):
        if self.head != None:
            while self.head.next != None:
                if (self.head.data == data):
                    return data
                self.head = self.head.next
            if(self.head.data == data):
                return self.head
        else:
            return None

    # Use this function to remove the specified Node from the LinkedList
    # Note that this function takes a Node (not data) as an argument.
    # Once the Node is removed, the list should still be able to be traversed - references will need to be updated to accomplish this task!
    # Think carefully about what needs to happen if the Node at the front of the list is removed, or if this node is the last Node in the list.
    def remove(self, node):
        temp = node.prev
        node.prev.next = node.next
        node.prevv = temp

# Use this class to represent a single element of the LinkedList
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
