class _Node:
    __slots__ = ("event", "next")
    def __init__(self, event):
        self.event = event
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, event):
        """Append at tail (O(1) with tail pointer)."""
        node = _Node(event)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            assert self.tail is not None
            self.tail.next = node
            self.tail = node
        self.size += 1

    def delete(self, event_id: int) -> bool:
        """Delete first node with event.id == event_id."""
        prev = None
        cur = self.head
        while cur:
            if cur.event.id == event_id:
                if prev:
                    prev.next = cur.next
                else:
                    # deleting head
                    self.head = cur.next
                if cur is self.tail:
                    # deleted tail -> update tail
                    self.tail = prev
                self.size -= 1
                return True
            prev = cur
            cur = cur.next
        return False

    def search_by_id(self, event_id: int):
        cur = self.head
        while cur:
            if cur.event.id == event_id:
                return cur.event
            cur = cur.next
        return None

    def list_all(self):
        res = []
        cur = self.head
        while cur:
            res.append(cur.event)
            cur = cur.next
        return res

    def _internal_state(self):
        # helpful for debugging: returns list of ids and size
        ids = []
        cur = self.head
        while cur:
            ids.append(cur.event.id)
            cur = cur.next
        return {
            "size": self.size,
            "ids": ids,
            "head_id": self.head.event.id if self.head else None,
            "tail_id": self.tail.event.id if self.tail else None
        }