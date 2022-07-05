"""
Creating a singly linked list,benefit is O(1) time 
for removing and inserting element in the middle of and array,prepend and append are also O(1)
"""


class ListNode:
    """
    A node in a singly-linked list.
    """

    def __init__(self, data=None, next=None):
        self.data = data
        self.next_node = next

    def __repr__(self):
        return repr(self.data)


class SinglyLinkedList:
    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head = None

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next_node
        return "[" + ", ".join(nodes) + "]"

    # return "->".join(nodes)

    def insert_at_head(self, data):
        """Add new Node containing data at head of the list
        Takes O(1) time
        """
        new_node = ListNode(data)
        new_node.next_node = self.head
        self.head = new_node

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        if not self.head:
            self.head = ListNode(data=data)
            return
        curr = self.head
        while curr.next_node:
            curr = curr.next_node
        curr.next = ListNode(data=data)

    def search(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) times
        Implemenation A
        """
        curr = self.head
        while curr:
            if curr.data == key:
                return curr
            else:
                curr = curr.next_node
        return None

        """ Implemenation B
        curr = self.head
        while curr AND curr.data != key:
             curr = curr.next
        return curr

        """

    def insert_at_position(self, data, index):
        """
        Insert a new Node into into a Singlylist at an index/particular postion takes O(1) time
        But finding the node at the insertion point takes O(n) time

        Therefore for Overall is O(n)
        """
        if index == 0:
            self.insert_at_head(data)
        if index > 0:
            new = ListNode(data)
            curr = self.head
            position = index
        while position > 1:
            curr = curr.next_node
            position -= 1

        previous_node = curr
        next = curr.next_node
        """ Inserting the new node """
        previous_node.next_node = new
        new.next_node = next

    def remove1(self, key):
        """
        Removes Node containing data that matches the key
        Returns the node or None  if key doesn't exist
        Takes O(n) times
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            # Scenario one
            if current.data and current == self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node

            else:
                previous = current
                current = current.next_node

        return current

    def remove2(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        # Find the element and keep a
        # reference to the element preceding it
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        # Unlink it from the list
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    def reverse(self):
        """
        Reverse the list in-place.
        Takes O(n) time.
        """
        curr = self.head
        prev_node = None
        next_node = None
        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        self.head = prev_node


l = SinglyLinkedList()
l.append(10)
l.append(20)
l.append(30)
l
