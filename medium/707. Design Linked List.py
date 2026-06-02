"""
707. Design Linked List
Medium
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 

Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
 

Constraints:

0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.

"""
class ListNode:
    def __init__(self, val=0, next=None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    ## Doubly Linked List Implementation
    
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and index == 0 and self.right != cur:
            return cur.val
        return -1
    def addAtHead(self, val: int) -> None:
        new_node, nxt, prev = ListNode(val), self.left.next, self.left
        prev.next = new_node
        nxt.prev = new_node
        new_node.prev = prev
        new_node.next = nxt

    def addAtTail(self, val: int) -> None:
        new_node, nxt, prev = ListNode(val), self.right, self.right.prev
        prev.next = new_node
        nxt.prev = new_node
        new_node.prev = prev
        new_node.next = nxt

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and index == 0:
            new_node, nxt, prev = ListNode(val), cur, cur.prev
            prev.next = new_node
            nxt.prev = new_node
            new_node.prev = prev
            new_node.next = nxt
        

    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and index == 0 and self.right != cur:
            nxt, prev = cur.next, cur.prev
            prev.next = nxt
            nxt.prev = prev
        

    ## Singly Linked List Implementation
    # def __init__(self):
    #     self.head = None

    # def get(self, index: int) -> int:
    #    if index < 0:
    #        return -1
    #    cur = self.head
    #    count = 0
    #    while cur:
    #     if count == index:
    #         return cur.val
    #     cur = cur.next
    #     count += 1       

    # def addAtHead(self, val: int) -> None:
    #     new_node = ListNode(val)
    #     new_node.next = self.head
    #     self.head = new_node

    # def addAtTail(self, val: int) -> None:
    #     new_node = ListNode(val)
    #     cur = self.head
    #     if not cur:
    #         self.head = new_node
    #     while cur.next:
    #         cur = cur.next
    #     cur.next = new_node
    #     new_node.next = None
    
    # def addAtIndex(self, index: int, val: int) -> None:
    #     new_node = ListNode(val)
    #     cur = self.head.next
    #     prev = self.head
    #     count = 0
    #     if index == 0:
    #         self.addAtHead(val)
    #     while cur:
    #         if count == index:
    #             print("inside", prev.val, cur.val, count)
    #             prev.next = new_node
    #             new_node.next = cur
    #         prev = cur
    #         cur = cur.next
    #         count += 1
        
    # def deleteAtIndex(self, index: int) -> None:
    #     cur = self.head.next
    #     prev = self.head
    #     count = 0
    #     if index == 0:
    #         self.head = self.head.next
    #     while cur:
    #         if count == index:
    #             prev.next = cur.next
    #         prev = cur
    #         cur = cur.next
    #         count += 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

input_func = ["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
input_val = [[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]

for func, val in zip(input_func, input_val):
    if func == "MyLinkedList":
        myLinkedList = MyLinkedList()
    elif func == "addAtHead":
        myLinkedList.addAtHead(val[0])
    elif func == "addAtTail":
        myLinkedList.addAtTail(val[0])
    elif func == "addAtIndex":
        myLinkedList.addAtIndex(val[0], val[1])
    elif func == "deleteAtIndex":
        myLinkedList.deleteAtIndex(val[0])
    elif func == "get":
        print(myLinkedList.get(val[0]))
    


# myLinkedList = MyLinkedList()
# myLinkedList.addAtHead(1)
# myLinkedList.addAtTail(3)
# myLinkedList.addAtIndex(1, 2)    # linked list becomes 1->2->3
# myLinkedList.get(1)              # return 2
# myLinkedList.deleteAtIndex(1)    # now the linked list is 1->3
# myLinkedList.get(1)              # return 3

cur = myLinkedList.left.next
while cur and cur != myLinkedList.right:
    print(cur.val, end=" -> " if cur.next != myLinkedList.right else "\n")
    cur = cur.next


