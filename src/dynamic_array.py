class DynamicArray:
    def __init__(self, initial_capacity: int = 2):
        if initial_capacity < 1:
            initial_capacity = 2
        self._capacity = initial_capacity
        self._size = 0
        self._buf = [None] * self._capacity

    def __len__(self):
        return self._size

    def _resize(self, new_capacity: int):
        new_buf = [None] * new_capacity
        for i in range(self._size):
            new_buf[i] = self._buf[i]
        self._buf = new_buf
        self._capacity = new_capacity

    def insert(self, event):
        """Append at end (like ArrayList.add)."""
        if self._size >= self._capacity:
            # double capacity
            self._resize(self._capacity * 2)
        self._buf[self._size] = event
        self._size += 1

    def delete(self, event_id: int) -> bool:
        """Delete first event with id == event_id. Return True if found+deleted."""
        # find index
        idx = -1
        for i in range(self._size):
            if self._buf[i].id == event_id:
                idx = i
                break
        if idx == -1:
            return False
        # shift left
        for j in range(idx, self._size - 1):
            self._buf[j] = self._buf[j + 1]
        self._buf[self._size - 1] = None
        self._size -= 1
        # optional: shrink when quarter full (keeps amortized bounds)
        if self._size > 0 and self._size <= self._capacity // 4:
            self._resize(max(2, self._capacity // 2))
        return True

    def search_by_id(self, event_id: int):
        for i in range(self._size):
            if self._buf[i].id == event_id:
                return self._buf[i]
        return None

    def list_all(self):
        return [self._buf[i] for i in range(self._size)]

    # convenience method for tests/inspection
    def _internal_state(self):
        return {
            "capacity": self._capacity,
            "size": self._size,
            "buffer": self._buf[:self._size]  # visible portion
        }