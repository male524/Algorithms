class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def getLen(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        length = self.getLen()
        if index + 1 > length:
            return -1
        if index == 0:
            return self.head.data
        else:
            temp = self.head.next
            for i in range(1, index + 1):
                if i == index:
                    return temp.data
                temp = temp.next

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        length = self.getLen()
        if index > length:
            return
        newNode = Node(val)
        if index == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            temp = self.head
            for i in range(1, index + 1):
                if i == index:
                    newNode.next = temp.next
                    temp.next = newNode
                temp = temp.next

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if self.head == None:
            return
        length = self.getLen()
        if index + 1 > length:
            return
        temp = self.head
        if index == 0:
            self.head = temp.next
            temp = None
        else:
            for i in range(index - 1):
                temp = temp.next
            nextAfter = temp.next.next
            temp.next = None
            temp.next = nextAfter
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)