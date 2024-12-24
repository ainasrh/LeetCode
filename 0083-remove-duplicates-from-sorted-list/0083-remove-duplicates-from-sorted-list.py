# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return None  # Return None if the list is empty

        current = head  # Start with the first node
        while current:
            runner = current  # Use a runner pointer to check for duplicates
            while runner.next:
                if runner.next.val == current.val:
                    runner.next = runner.next.next  # Remove duplicate
                else:
                    runner = runner.next  # Move runner to the next node
            current = current.next  # Move to the next node

        return head  # Return the modified linked list

            