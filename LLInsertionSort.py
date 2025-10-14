    def insertionSort(self):
        # edge case to return none and do nothing if the linked list on has one node or no elements at all
        if self.head is None or self.head.next is None:
            return None
    
        sorted_head = None
        current = self.head
    
        while current is not None:
            next_node = current.next
    
            # Parse date+time once for current node
            c_key = datetime.strptime(current.event["date"] + " " + current.event["start_time"],"%Y-%m-%d %H:%M")
    
            if sorted_head is None:
                current.next = None
                sorted_head = current
            else:
                # Compare with sorted_head
                s_key = datetime.strptime(sorted_head.event["date"] + " " + sorted_head.event["start_time"],"%Y-%m-%d %H:%M")
    
                if c_key < s_key:
                    current.next = sorted_head
                    sorted_head = current
                else:
                    search = sorted_head
                    while search.next is not None:
                        n_key = datetime.strptime(
                            search.next.event["date"] + " " + search.next.event["start_time"],
                            "%Y-%m-%d %H:%M"
                        )
                        if c_key < n_key:
                            break
                        search = search.next
                    current.next = search.next
                    search.next = current
            current = next_node
        self.head = sorted_head                  
                      
