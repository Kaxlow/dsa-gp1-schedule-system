    def quickSort(self):
         
        #sorting through date + start_time
    
        def partition(head):
            # need to have the partition of the list around the pivot; return (left, pivot, right).
            if head is None or head.next is None:
                return None, head, None
    
            pivot = head
            pivot_key = datetime.strptime(
                pivot.event["date"] + " " + pivot.event["start_time"], "%Y-%m-%d %H:%M"
            )
    
            left_head = left_tail = None
            right_head = right_tail = None
    
            cur = head.next
            while cur:
                cur_key = datetime.strptime(
                    cur.event["date"] + " " + cur.event["start_time"], "%Y-%m-%d %H:%M"
                )
                nxt = cur.next
                cur.next = None
    
                if cur_key < pivot_key:
                    if left_head is None:
                        left_head = left_tail = cur
                    else:
                        left_tail.next = cur
                        left_tail = cur
                else:
                    if right_head is None:
                        right_head = right_tail = cur
                    else:
                        right_tail.next = cur
                        right_tail = cur
                cur = nxt
    
            return left_head, pivot, right_head
    
        def sort(head):
            if head is None or head.next is None:
                return head, head  # (head, tail)
    
            left, pivot, right = partition(head)
    
            left_head, left_tail = sort(left) if left else (None, None)
            right_head, right_tail = sort(right) if right else (None, None)
    
            # Connect left -> pivot -> right
            new_head = left_head if left_head else pivot
            if left_tail:
                left_tail.next = pivot
            pivot.next = right_head
            new_tail = right_tail if right_tail else pivot
    
            return new_head, new_tail
    
        # Start the recursive quicksort
        self.head, _ = sort(self.head)
