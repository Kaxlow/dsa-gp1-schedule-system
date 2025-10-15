from datetime import datetime 
import copy
class LinkedListNode:
  def __init__(self, event):
    self._value = event
    self._next = None

class LinkedList:
    def __init__(self):
        self._head = None
        self._total = 0
    
      
    def insertionSort(self):
    #creating a new linked list to have the sorted events
        sortedEvents = LinkedList()
        cur = self._head
        while cur:
            ev = cur._value
            # Create a fresh node for the sorted list
            node = LinkedListNode(ev)
            key_dt = datetime.strptime(ev["date"] + " " + ev["start_time"], "%Y-%m-%d %H:%M")

            if sortedEvents._head is None:
                # First node in sorted list
                sortedEvents._head = node
            else:
                # Compare against head
                head_ev = sortedEvents._head._value
                head_dt = datetime.strptime(
                    head_ev["date"] + " " + head_ev["start_time"], "%Y-%m-%d %H:%M"
                )
                if key_dt < head_dt:
                    # Insert before head
                    node._next = sortedEvents._head
                    sortedEvents._head = node
                else:
                    spot = sortedEvents._head
                    # Find insertion point
                    while spot._next:
                        next_ev = spot._next._value
                        next_dt = datetime.strptime(
                            next_ev["date"] + " " + next_ev["start_time"], "%Y-%m-%d %H:%M"
                        )
                        if key_dt < next_dt:
                            break
                        spot = spot._next
                    # Insert after spot
                    node._next = spot._next
                    spot._next = node

            sortedEvents._total += 1
            cur = cur._next

        return sortedEvents

    def mergeSort(self):

        def divide(head, count):
            # Splits first count nodes into two halves
            if count <= 1:
                return head, None
            mid = count // 2
            prev, cur = None, head
            for _ in range(mid):
                prev, cur = cur, cur._next
            prev._next = None
            # head = first half, cur = second half
            return head, cur

        def merge(a, b):
            if a is None: 
                return b
            if b is None:
                return a
            a_dt = datetime.strptime(a._value["date"] + " " + a._value["start_time"], "%Y-%m-%d %H:%M")
            b_dt = datetime.strptime(b._value["date"] + " " + b._value["start_time"], "%Y-%m-%d %H:%M")
            if a_dt <= b_dt:
                a._next = merge(a._next, b)
                return a
            else:
                b._next = merge(a, b._next)
                return b

        def sort_sublist(head, count):
            if count <= 1:
                return head
            left_head, right_head = divide(head, count)
            left_sorted = sort_sublist(left_head, count // 2)
            right_sorted = sort_sublist(right_head, count - count // 2)
            return merge(left_sorted, right_sorted)

        # Copy events into fresh nodes
        temp_head = None
        temp_tail = None
        cur = self._head
        while cur:
            node = LinkedListNode(cur._value)
            if not temp_head:
                temp_head = node
                temp_tail = node
            else:
                temp_tail._next = node
                temp_tail = node
            cur = cur._next

        # Sort using known total
        sorted_head = sort_sublist(temp_head, self._total)

        # Build new LinkedList wrapper
        new_list = LinkedList()
        new_list._head = sorted_head
        new_list._total = self._total  # same number of nodes

        return new_list

    def quickSort(self):
        """
        Return a NEW LinkedList sorted by date+start_time.
        Original list remains unchanged.
        """
        # 1. Clone the original chain into a fresh set of nodes
        clone_head = None
        clone_tail = None
        cur = self._head
        while cur:
            node = LinkedListNode(cur._value)
            if not clone_head:
                clone_head = clone_tail = node
            else:
                clone_tail._next = node
                clone_tail = node
            cur = cur._next

        # 2. Partition around pivot; return (left, pivot, right)
        def partition(head):
            if head is None or head._next is None:
                return None, head, None
            pivot = head
            pivot_dt = datetime.strptime(
                pivot._value["date"] + " " + pivot._value["start_time"],
                "%Y-%m-%d %H:%M"
            )
            left_head = left_tail = None
            right_head = right_tail = None
            cur = head._next
            while cur:
                nxt = cur._next
                cur._next = None
                cur_dt = datetime.strptime(
                    cur._value["date"] + " " + cur._value["start_time"],
                    "%Y-%m-%d %H:%M"
                )
                if cur_dt < pivot_dt:
                    if not left_head:
                        left_head = left_tail = cur
                    else:
                        left_tail._next = cur
                        left_tail = cur
                else:
                    if not right_head:
                        right_head = right_tail = cur
                    else:
                        right_tail._next = cur
                        right_tail = cur
                cur = nxt
            return left_head, pivot, right_head

        # 3. Recursively sort a chain; return (new_head, new_tail)
        def sort_chain(head):
            if head is None or head._next is None:
                return head, head
            left, pivot, right = partition(head)
            lh, lt = sort_chain(left) if left else (None, None)
            rh, rt = sort_chain(right) if right else (None, None)
            new_head = lh if lh else pivot
            if lt:
                lt._next = pivot
            pivot._next = rh
            new_tail = rt if rt else pivot
            return new_head, new_tail

        # 4. Sort the cloned chain
        sorted_head, _ = sort_chain(clone_head)

        # 5. Wrap sorted chain in a new LinkedList
        new_list = LinkedList()
        new_list._head = sorted_head
        new_list._total = self._total
        return new_list


  
