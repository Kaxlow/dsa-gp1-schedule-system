#src/array_list.py

class ArrayList:
    def init(self):
        self.capacity = 2
        self.size = 0
        self.events = [None] * self.capacity
    
    def _resize(self):
        self.capacity *= 2
        new_array_list = [None] * self.capacity
        for i in range(self.size):
            new_array_list[i] = self.events[i]
        self.events = new_array_list
    
    def insert(self, event):
        if self.size == self.capacity:
            self._resize()
        self.events[self.size] = event
        self.size += 1

    def delete(self, event_id):
        for i in range(self.size):
            if self.events[i]["id"] == event_id:
                for j in range(i, self.size - 1):
                    self.events[j] = self.events[j+1]
                
                self.events[self.size - 1] = None
                self.size -= 1

                return True
        return False
    
    def search_by_id(self, event_id):
        for i in range(self.size):
            if self.events[i]["id"] == event_id:
                return self.events[i]

        return None    
    
    def list_all(self):
        return [self.events[i] for i in range(self.size)]