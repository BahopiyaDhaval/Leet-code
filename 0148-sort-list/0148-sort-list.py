# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
   
        if not head or not head.next:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

       
        mid = slow.next
        slow.next = None

      
        left = self.sortList(head)
        right = self.sortList(mid)

 
        return self.merge(left, right)

    def merge(self, a, b):
        dummy = ListNode(0)
        current = dummy

        while a and b:
            if a.val < b.val:
                current.next = a
                a = a.next
            else:
                current.next = b
                b = b.next

            current = current.next

        if a:
            current.next = a
        else:
            current.next = b

        return dummy.next