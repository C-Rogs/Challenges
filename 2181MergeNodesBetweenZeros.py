# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#My solution uses pointers but it could also be done recursively merging all untill 0 until there is none left. 
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        upcoming = head.next
        total = 0

        while upcoming:
            print(current.val)
            current.next.val += current.val
        
            if upcoming.val == 0:
                current = current.next
                current.val = total
                total = 0
            else:
                total += upcoming.val
            upcoming = upcoming.next

        current.next = None
        return head.next