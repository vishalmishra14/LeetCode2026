"""
23. Merge k Sorted Lists
Solved

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.

"""
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoList(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merge_l = ListNode(0)
        cur = merge_l

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        return merge_l.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i + 1 < len(lists) else None
                merged.append(self.mergeTwoList(list1, list2))
            lists = merged
        return lists[0]

s= Solution()
# create linked list from array
def create_linked_list(arr):
    if not arr or len(arr) == 0:
        return None
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
lists = [[1,4,5],[1,3,4],[2,6]]
linked_lists = [create_linked_list(l) for l in lists]
print_linked_list(s.mergeKLists(linked_lists)) # 1 1 2 3 4 4 5 6
lists = []
linked_lists = [create_linked_list(l) for l in lists]
print_linked_list(s.mergeKLists(linked_lists)) # []
lists = [[]]
linked_lists = [create_linked_list(l) for l in lists]
print_linked_list(s.mergeKLists(linked_lists)) # []


        