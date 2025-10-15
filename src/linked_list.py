class Node:
    def __init__(self, event):
        self.event = event
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, event):
        new_node = Node(event)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head

        while curr.next is not None:
            curr = curr.next
        
        curr.next = new_node
        
    def delete(self, event_id):
        curr = self.head
        prev = None

        while curr:
            if curr.event["id"] == event_id:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return True
        
        prev = curr
        cur = curr.next

        return False

    def search_by_id(self, event_id):
        curr = self.head
        while curr:
            if curr.event["id"] == event_id:
                return curr.event
            curr = curr.next

        return None
    
    def list_all(self):
        result = []
        curr = self.head()
        while curr:
            result.append(curr.event)
            cur = curr.next

        return result

