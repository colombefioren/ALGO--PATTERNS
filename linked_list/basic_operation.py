class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedListBasicOps:
    """Basic Linked List Operations Pattern"""
    
    def __init__(self):
        self.head = None
    
    # === INSERTION OPERATIONS ===
    
    def insert_at_head(self, val):
        """Insert node at the beginning - O(1)"""
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_tail(self, val):
        """Insert node at the end - O(n)"""
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def insert_at_position(self, val, position):
        """Insert node at specific position (0-indexed) - O(n)"""
        if position == 0:
            self.insert_at_head(val)
            return
        
        new_node = ListNode(val)
        current = self.head
        count = 0
        
        while current and count < position - 1:
            current = current.next
            count += 1
        
        if not current:
            raise IndexError("Position out of bounds")
        
        new_node.next = current.next
        current.next = new_node
    
    def insert_after_value(self, val, target_val):
        """Insert after first occurrence of target value - O(n)"""
        current = self.head
        while current and current.val != target_val:
            current = current.next
        
        if current:
            new_node = ListNode(val)
            new_node.next = current.next
            current.next = new_node
    
    # === DELETION OPERATIONS ===
    
    def delete_at_head(self):
        """Delete first node - O(1)"""
        if self.head:
            self.head = self.head.next
    
    def delete_at_tail(self):
        """Delete last node - O(n)"""
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
    
    def delete_by_value(self, val):
        """Delete first occurrence of value - O(n)"""
        if not self.head:
            return
        
        # Handle head deletion separately
        if self.head.val == val:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next and current.next.val != val:
            current = current.next
        
        if current.next:
            current.next = current.next.next
    
    def delete_at_position(self, position):
        """Delete node at specific position (0-indexed) - O(n)"""
        if position == 0:
            self.delete_at_head()
            return
        
        current = self.head
        count = 0
        
        while current and count < position - 1:
            current = current.next
            count += 1
        
        if not current or not current.next:
            raise IndexError("Position out of bounds")
        
        current.next = current.next.next
    
    # === SEARCH & TRAVERSAL ===
    
    def search(self, val):
        """Search for value - O(n)"""
        current = self.head
        while current:
            if current.val == val:
                return True
            current = current.next
        return False
    
    def get_length(self):
        """Get length of linked list - O(n)"""
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length
    
    def get_node_at(self, index):
        """Get node at specific index - O(n)"""
        current = self.head
        count = 0
        while current and count < index:
            current = current.next
            count += 1
        return current
    
    def print_list(self):
        """Print the linked list"""
        current = self.head
        elements = []
        while current:
            elements.append(str(current.val))
            current = current.next
        print(" -> ".join(elements) if elements else "Empty list")
    
    # === UTILITY OPERATIONS ===
    
    def to_array(self):
        """Convert linked list to array"""
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    @staticmethod
    def from_array(arr):
        """Create linked list from array"""
        ll = LinkedListBasicOps()
        for val in arr:
            ll.insert_at_tail(val)
        return ll

# Example usage
print("=== Basic Operations ===")
ll = LinkedListBasicOps()
ll.insert_at_tail(1)
ll.insert_at_tail(2)
ll.insert_at_tail(3)
ll.insert_at_head(0)
ll.print_list()  # 0 -> 1 -> 2 -> 3

ll.delete_by_value(2)
ll.print_list()  # 0 -> 1 -> 3

print(f"Length: {ll.get_length()}")  # 3
print(f"Search 3: {ll.search(3)}")  # True
print(f"Array: {ll.to_array()}")  # [0, 1, 3]