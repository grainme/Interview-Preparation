"""
This code would indeed check whether we have a cycle in our linked list.
But we won't know the starting node of that cycle. For that we use what's
called Floyd Algorithm.

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        slow, fast = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            print(fast.val, slow.val, sep = " ")
            if fast == slow:
                return fast
            
        return None 

Floyd's Cycle Detection Algorithm, also known as the Tortoise and Hare algorithm, is a pointer-based algorithm used to detect cycles in a sequence, most commonly in linked lists. It operates with two pointers, a "slow" pointer (tortoise) and a "fast" pointer (hare), moving at different speeds.
Algorithm Steps:

Initialization:
Initialize a slow pointer and a fast pointer, both pointing to the head of the sequence (e.g., linked list).

Cycle Detection:
Move the slow pointer one step at a time (slow = slow.next).
Move the fast pointer two steps at a time (fast = fast.next.next).
Continue this movement until one of two conditions is met:
- No cycle: The fast pointer reaches the end of the sequence (becomes null), indicating no cycle is present.
- Cycle detected: The slow and fast pointers meet at the same node, indicating a cycle exists.

Finding the Cycle Entry Point (Our Problem):
If a cycle is detected, to find the starting node of the cycle:
Reset the slow pointer back to the head of the sequence.
Keep the fast pointer at its meeting point.
Move both slow and fast pointers one step at a time until they meet again. This meeting point will be the entry point of the cycle.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        slow, fast = head, head
        cyclic = False
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            print(fast.val, slow.val, sep = " ")
            if fast == slow:
                cyclic = True
                break

        if not cyclic:
            return None
        # Second part of Floyd starts here
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow 
