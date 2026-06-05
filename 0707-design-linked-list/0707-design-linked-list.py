class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MyLinkedList(object):

    def __init__(self):
        self.head = ListNode(0)
        self.size = 0
        

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """

        if index < 0 or index >= self.size:
            return -1
        pred = self.head.next
        for _ in range(index):
            pred = pred.next
        return pred.val
  

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0,val)
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size,val)
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size:
            return

        if index<0:
            index = 0

        self.size += 1
        pred = self.head

        for _ in range(index):
            pred = pred.next
        addnode = ListNode(val)
        addnode.next = pred.next
        pred.next = addnode
        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        self.size -= 1        
        pred = self.head

        for _ in range(index):
            pred = pred.next
        pred.next = pred.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)