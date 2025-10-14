    def mergeSort(self):
        # expectation is to sort by date + start_time
        # edge to do nothing and just return the linked list if it contains no element or one element
        if self.head is None or self.head.next is None:
            return  # nothing to sort
    
        def divide(head):
            # We need to split the linked list to make sure that it is divided into two halves.
            # We calculate the count of events available in the linked list and take the median value
            # if the Linked list is empty or has only one node,
            if head is None or head.next is None:
                return head, None
            cnt = 0
            # count of events initialised to be 0, storing head value to an other variable to not lose it
            curr = head
            while curr is not None:
                cnt += 1
                curr = curr.next
            # identify the median of the linked list to find the middle node and perform partition there
            mid = cnt//2
            #need to identify the node right before we hit the middle node, so consider the prev constant
            curr = head
            prev = None
            for _ in range(mid):
                prev = curr
                curr = curr.next
            # now our current node is considered to have the first node of the second half
            firstPart = head
            secondPart = current
            # end the first part here itself with prev node.
            prev.next = None 
            return firstPart, secondPart
                  def merge(head, second):
            # we use recursion to merge both parts of the linked lists
            if head is None:
                return second
            if second is None:
                return head
            # comparing the event date + start_time for both the events
            headTime = datetime.strptime(head.event["date"] + " " + head.event["start_time"], "%Y-%m-%d %H:%M")
            secondTime = datetime.strptime(second.event["date"] + " " + second.event["start_time"], "%Y-%m-%d %H:%M")
            
            # now we recursively call the other both the parts of the linked list to make sure we parse through them all
            if headTime <= secondTime:
                head.next = merge(head.next,second)
                return head
            else:
                second.next = merge(head,second.next)
                return second

        def sort(head):
            if head is None or head.next is None:
                return head
            head, second = divide(head)     
            head = sort(head)             
            second = sort(second)
            return merge(head, second)    
            
        self.head = sort(self.head)
