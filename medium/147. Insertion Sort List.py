"""
147. Insertion Sort List
Medium
Topics
premium lock icon
Companies
Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:

Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
It repeats until no input elements remain.
The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.


 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
 

Constraints:

The number of nodes in the list is in the range [1, 5000].
-5000 <= Node.val <= 5000

"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(0)
        prev.next = cur = head
        while head and head.next:
            if head.val > head.next.val:
                cur = head.next
                curPre = prev
                while curPre.next.val < cur.val:
                    curPre = curPre.next
                head.next = cur.next
                cur.next = curPre.next
                curPre.next = cur
            else:
                head = head.next
        return prev.next

        # cur = head
        # while cur and cur.next:
        #     if cur.val > cur.next.val:
        #         # find the position to insert
        #         pre = ListNode(0)
        #         pre.next = head
        #         while pre.next and pre.next.val < cur.next.val:
        #             pre = pre.next
        #         # insert cur.next after pre
        #         temp = pre.next
        #         pre.next = cur.next
        #         cur.next = cur.next.next
        #         pre.next.next = temp
        #     else:
        #         cur = cur.next
        # return head
    
s = Solution()
# create linked list from array
def create_linked_list(arr):
    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return head
# print linked list
def print_linked_list(head):
    cur = head
    while cur:
        print(cur.val, end=' ')
        cur = cur.next
    print()
head = create_linked_list([4,2,1,3])
print_linked_list(s.insertionSortList(head)) # 1 2 3 4
head = create_linked_list([-1,5,3,4,0])
print_linked_list(s.insertionSortList(head)) # -1 0 3 4 5
