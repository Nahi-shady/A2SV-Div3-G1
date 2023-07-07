class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class MyLinkedList(object):

    def __init__(self, ):
        self.head = None
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        for i in range(index):
            curr = curr.next
            
        return curr.val
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.head = Node(val, self.head)
        self.size += 1      

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.head:
            self.head = Node(val)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(val)
        self.size += 1
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size:
            return
        if index <= 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            curr.next = Node(val, curr.next)
            self.size += 1
        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next
        self.size -= 1