# src/sorts_linked_list.py

from src.linked_list import Node, LinkedList

def event_key(event):
    y, mo, d = map(int, event["date"].split("-"))
    hh, mm = map(int, event["time"].split(":"))
    return (y, mo, d, hh, mm)

#Insertion Sort 
def insertion_sort_linked_list(ll):
    if ll.head is None or ll.head.next is None:
        return ll

    sorted_head = None

    curr = ll.head
    while curr:
        next_curr = curr.next
        # insert curr into sorted list
        if (sorted_head is None) or (event_key(curr.event) < event_key(sorted_head.event)):
            curr.next = sorted_head
            sorted_head = curr
        else:
            spot = sorted_head
            while spot.next and event_key(spot.next.event) <= event_key(curr.event):
                spot = spot.next
            curr.next = spot.next
            spot.next = curr
        curr = next_curr

    ll.head = sorted_head
    return ll

#Merge Sort
def split_middle(head):
    if head is None or head.next is None:
        return head, None
    
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    middle = slow.next
    slow.next = None

    return head, middle

def merge_sorted_lists(l1, l2):
    dummy = Node(None)
    tail = dummy
    while l1 and l2:
        if event_key(l1.event) <= event_key(l2.event):
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 else l2

    return dummy.next

def merge_sort_linked_list_head(head):
    if head is None or head.next is None:
        return head
    left, right = split_middle(head)
    left_sorted = merge_sort_linked_list_head(left)
    right_sorted = merge_sort_linked_list_head(right)
    return merge_sorted_lists(left_sorted, right_sorted)

def merge_sort_linked_list(ll):
    ll.head = merge_sort_linked_list_head(ll.head)
    return ll

#Quick Sort
def concat_three(a_head, a_tail, b_head, b_tail):
    if a_head is None:
        return b_head, b_tail
    a_tail.next = b_head
    return a_head, b_tail if b_tail else a_tail

def quick_sort_linked_list(ll):
    def quick_sort_head(head):
        if head is None or head.next is None:
            # find tail
            tail = head
            return head, tail
        # choose pivot as head's key (simple deterministic choice)
        pivot_key = event_key(head.event)
        # create heads/tails for less, equal, greater
        less_h = less_t = None
        equal_h = equal_t = None
        greater_h = greater_t = None

        # partition
        curr = head
        while curr:
            next_node = curr.next
            curr.next = None
            k = event_key(curr.event)
            if k < pivot_key:
                if less_h is None:
                    less_h = less_t = curr
                else:
                    less_t.next = curr
                    less_t = curr
            elif k == pivot_key:
                if equal_h is None:
                    equal_h = equal_t = curr
                else:
                    equal_t.next = curr
                    equal_t = curr
            else:
                if greater_h is None:
                    greater_h = greater_t = curr
                else:
                    greater_t.next = curr
                    greater_t = curr
            curr = next_node

        # recursively sort less and greater
        sorted_less_h, sorted_less_t = (None, None)
        sorted_greater_h, sorted_greater_t = (None, None)
        if less_h:
            sorted_less_h, sorted_less_t = quick_sort_head(less_h)
        if greater_h:
            sorted_greater_h, sorted_greater_t = quick_sort_head(greater_h)

        # now concatenate: less + equal + greater
        head_res = tail_res = None
        if sorted_less_h:
            head_res = sorted_less_h
            tail_res = sorted_less_t
        if equal_h:
            if head_res is None:
                head_res = equal_h
                tail_res = equal_t
            else:
                tail_res.next = equal_h
                tail_res = equal_t
        if sorted_greater_h:
            if head_res is None:
                head_res = sorted_greater_h
                tail_res = sorted_greater_t
            else:
                tail_res.next = sorted_greater_h
                tail_res = sorted_greater_t

        return head_res, tail_res

    new_head, _ = quick_sort_head(ll.head)
    ll.head = new_head
    return ll

