class ReverseLinkedList:
    """Reverse Linked List Pattern"""
    
    @staticmethod
    def reverse_iterative(head):
        """
        Reverse entire linked list iteratively.
        
        Time: O(n), Space: O(1)
        """
        prev = None
        current = head
        
        while current:
            next_node = current.next  # Store next
            current.next = prev       # Reverse link
            prev = current            # Move prev forward
            current = next_node       # Move current forward
        
        return prev
    
    @staticmethod
    def reverse_recursive(head):
        """
        Reverse entire linked list recursively.
        
        Time: O(n), Space: O(n) due to recursion
        """
        # Base case
        if not head or not head.next:
            return head
        
        # Reverse rest of the list
        new_head = ReverseLinkedList.reverse_recursive(head.next)
        
        # Put current head at the end
        head.next.next = head
        head.next = None
        
        return new_head
    
    @staticmethod
    def reverse_between(head, left, right):
        """
        Reverse nodes from position left to right (1-indexed).
        
        Time: O(n), Space: O(1)
        """
        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Move to node before reversal start
        for _ in range(left - 1):
            prev = prev.next
        
        # Reverse using 3 pointers
        current = prev.next
        for _ in range(right - left):
            next_node = current.next
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
        
        return dummy.next
    
    @staticmethod
    def reverse_in_groups(head, k):
        """
        Reverse nodes in groups of k.
        
        Time: O(n), Space: O(1)
        """
        if not head or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy
        
        while True:
            # Check if there are k nodes remaining
            kth = prev_group
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            
            # Reverse k nodes
            group_start = prev_group.next
            next_group = kth.next
            
            # Reverse current group
            prev = next_group
            current = group_start
            while current != next_group:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            
            # Connect with previous group
            temp = prev_group.next
            prev_group.next = prev
            prev_group = temp
    
    @staticmethod
    def swap_pairs(head):
        """
        Swap every two adjacent nodes.
        
        Time: O(n), Space: O(1)
        """
        if not head or not head.next:
            return head
        
        # New head will be second node
        new_head = head.next
        
        prev = None
        current = head
        
        while current and current.next:
            next_pair = current.next.next
            second = current.next
            
            # Swap
            second.next = current
            current.next = next_pair
            
            if prev:
                prev.next = second
            
            prev = current
            current = next_pair
        
        return new_head

# Example usage
print("\n=== Reverse Linked List ===")
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
reversed_head = ReverseLinkedList.reverse_iterative(head)
# Print reversed: 5 -> 4 -> 3 -> 2 -> 1
current = reversed_head
while current:
    print(current.val, end=" -> " if current.next else "")
    current = current.next
print()

# Reverse between
head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
reversed_between = ReverseLinkedList.reverse_between(head2, 2, 4)
# Should be: 1 -> 4 -> 3 -> 2 -> 5