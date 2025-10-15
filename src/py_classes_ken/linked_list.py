# Import modules
from datetime import datetime, time
from .utils import get_event_dt_start, get_event_dt_end

# Define class for nodes in linked list
class LinkedListNode:
  def __init__(self, event):
    self._value = event
    self._next = None

# Define class for linked list
class LinkedList:
  def __init__(self):
    self._head = None
    self._total = 0

  # Sort algorithms

  # Outer sort function will call one of 3 inner sort functions (_insertion_sort, _merge_sort, _quick_sort) depending on which is specified as argument
  # Sort by date-time as default, can alternatively sort by event ID

  # Define helper function to set sort attribute for comparison in sort algorithms
  def _set_sort_attr(self, event, sort_by):
    if sort_by == "date-time":
      return get_event_dt_start(event)
    elif sort_by == "id":
      return event["id"]
    else:
      return "Error: Must sort by \"date-time\" or \"id\"."

  # Insertion sort. By default, sort by event date and time.
  def _insertion_sort(self, sort_by = "date-time"):
    # Proceed only if there are at least 2 nodes in linked list, else return self
    if self._total >= 2:
      # Starting from second-left element, take each element and insert into sorted array
      for outer in range(1, self._total):
        # Save outer element to insert into sorted array. Start from head and move to outer node
        current_node = self._head
        for i in range(outer):
          current_node = current_node._next
        outer_node = current_node
        # Mark the inner node which is just before the outer node. Inner node is the last node of the sorted section
        inner = outer - 1
        # Save inner element
        current_node = self._head
        for i in range(inner):
          current_node = current_node._next
        inner_node = current_node
        # While new element's sort-by attribute is smaller than sorted section element's corresponding attribute, check against the next left inner node
        while inner >= 0 and self._set_sort_attr(outer_node._value, sort_by) < self._set_sort_attr(inner_node._value, sort_by):
          # Set node to left of inner node as new inner node to check against
          inner -= 1
          # If inner is at index -1, that means inner node is None and outer node will be inserted before head, i.e., outer node is smaller than all nodes in sorted section
          if inner == -1:
            inner_node = None
          else:
            current_node = self._head
            for i in range(inner):
              current_node = current_node._next
            inner_node = current_node
        # When the next inner node's sort-by attribute is not larger than the outer node's sort-by attribute, insert the outer node after this inner node
        # First, move to node before outer node
        current_node = self._head
        for i in range(outer - 1):
          current_node = current_node._next
        # Point the node before outer node to the node after outer node
        current_node._next = current_node._next._next
        # If inserting outer node before head, when inner_node is None
        if inner_node is None:
          # point outer node to the existing head
          outer_node._next = self._head
          # Make outer node the new head
          self._head = outer_node
        # If not inserting outer node before head
        else: 
          # Next, point outer node to the node after the inner node
          outer_node._next = inner_node._next
          # Point inner node to outer node
          inner_node._next = outer_node
    return self
  
  # Merge sort. By default, sort by event date and time
  def _merge_sort(self, sort_by = "date-time"):
    # Base case: if list has zero or one element, it's already sorted; return self
    if self._total <= 1:
      return self

    # Split into left and right lists if current list has multiple elements
    if self._total > 1:
      # Start from head and move to midpoint node
      current_node = self._head
      for i in range(self._total // 2 - 1):
        current_node = current_node._next
      # Create right list as a new linked list starting from node after midpoint node and ending at tail node
      right_list = LinkedList()
      right_list._head = current_node._next
      # Set right_list's length
      right_list._total = self._total - (self._total // 2 - 1) - 1
      # Turn current list into left list by truncating current list at midpoint node
      current_node._next = None
      left_list = self
      # Set left_list's length
      left_list._total = self._total // 2 - 1 + 1
      # Split into left and right lists recursively by calling merge_sort() again
      # Capture and use the returned sorted lists — recursive calls may produce new LinkedList
      left_list = left_list._merge_sort(sort_by)
      right_list = right_list._merge_sort(sort_by)
      # Merge splits lists in sort order
      # Initialize sorted linked list
      self = LinkedList()
      # While both left_list and right_list still have un-merged nodes
      while left_list._head is not None and right_list._head is not None:
        # If left_list's head's sort-by attribute <= right_list's head's sort-by attribute, left_list's head becomes the next node in sorted linked list
        if left_list._set_sort_attr(left_list._head._value, sort_by) <= right_list._set_sort_attr(right_list._head._value, sort_by):
          # Save left_list's head to new node to add to sorted linked list
          new_node = left_list._head
          # Make left_list's next node the new head
          left_list._head = left_list._head._next
          left_list._total -= 1
        # If right_list's head's sort-by attribute < left_list's head's sort-by attribute, right_list's head becomes the next node in sorted linked list
        else:
          # Save right_list's head to new node to add to sorted linked list
          new_node = right_list._head
          # Make left_list's next node the new head
          right_list._head = right_list._head._next
          right_list._total -= 1
        # Disconnect new node from its former linked list
        new_node._next = None
        # If sorted linked list is empty, make new node the sorted linked list's head
        if self._head is None:
          self._head = new_node
        # Else insert new node after tail of sorted linked list
        else:
          current_node = self._head
          while current_node._next:
            current_node = current_node._next
          current_node._next = new_node
        self._total += 1
      # While only left_list has un-merged nodes
      while left_list._head is not None:
        # Save left_list's head to new node to add to sorted linked list
        new_node = left_list._head
        # Make left_list's next node the new head
        left_list._head = left_list._head._next
        left_list._total -= 1
        # Disconnect new node from its former linked list
        new_node._next = None
        # If sorted linked list is empty, make new node the sorted linked list's head
        if self._head is None:
          self._head = new_node
        # Else insert new node after tail of sorted linked list
        else:
          current_node = self._head
          while current_node._next:
            current_node = current_node._next
          current_node._next = new_node
        self._total += 1
      # While only right_list has un-merged elements
      while right_list._head is not None:
        # Save right_list's head to new node to add to sorted linked list
        new_node = right_list._head
        # Make left_list's next node the new head
        right_list._head = right_list._head._next
        right_list._total -= 1
        # Disconnect new node from its former linked list
        new_node._next = None
        # If sorted linked list is empty, make new node the sorted linked list's head
        if self._head is None:
          self._head = new_node
        # Else insert new node after tail of sorted linked list
        else:
          current_node = self._head
          while current_node._next:
            current_node = current_node._next
          current_node._next = new_node
        self._total += 1
      return self
    
  # Quick sort. By default, sort by event date and time
  def _quick_sort(self, sort_by = "date-time"):
    # Base case: return linked list unchanged if there's zero or one element
    if self._total <= 1:
      return self
    else:
      # Select node at median position as pivot
      # Start from head and move to node at median position
      current_node = self._head
      for i in range(self._total // 2 - 1):
        current_node = current_node._next
      pivot_node = current_node
      # Move each element into sub-lists by comparing against pivot
      smaller = LinkedList()
      center = LinkedList()
      larger = LinkedList()
      # Starting from head, compare each node event's sort-by attribute against the pivot node event's sort-by attribute, then move out of original linked list into smaller, center, or larger
      while self._head is not None:
        current_node = self._head
        # Save next node before disconnecting current node
        next_node = current_node._next
        # Disconnect current node from the original list
        current_node._next = None
        # Update head to next node in original list
        self._head = next_node
        self._total -= 1
        # If event's sort-by attribute is smaller than pivot event's sort-by attribute, move node to smaller list
        if self._set_sort_attr(current_node._value, sort_by) < self._set_sort_attr(pivot_node._value, sort_by):
          # Set as head of smaller list if smaller list is empty
          if smaller._head is None:
            smaller._head = current_node
            smaller._total += 1
          else:
            # Else, move to end of smaller list, then append current_node
            smaller_current_node = smaller._head
            while smaller_current_node._next is not None:
              smaller_current_node = smaller_current_node._next
            smaller_current_node._next = current_node
            smaller._total += 1
        # If event's sort-by attribute is larger than pivot event's sort-by attribute, move node to larger list
        elif self._set_sort_attr(current_node._value, sort_by) > self._set_sort_attr(pivot_node._value, sort_by):
          # Set as head of larger list if larger list is empty
          if larger._head is None:
            larger._head = current_node
            larger._total += 1
          else:
            # Else, move to end of larger list, then append current_node
            larger_current_node = larger._head
            while larger_current_node._next is not None:
              larger_current_node = larger_current_node._next
            larger_current_node._next = current_node
            larger._total += 1
        # If event's sort-by attribute is equal to pivot event's sort-by attribute, move node to center list. More than one nodes can match the pivot node
        else:
          # Set as head of center list if center list is empty
          if center._head is None:
            center._head = current_node
            center._total = 1
          else:
            # Else, move to end of larger list, then append current_node
            center_current = center._head
            while center_current._next is not None:
              center_current = center_current._next
            center_current._next = current_node
            center._total += 1
      # Recursively split sub-lists around new pivots until no longer possible
      # Rejoin split arrays in order of smaller, center, larger
      self._head = smaller._quick_sort(sort_by)._head
      self._total = 0
      # If smaller is empty, make center head the new head since center will have at least the pivot node
      if self._head is None:
        self._head = center._head
        # Move to tail of center list
        current_node = self._head
        self._total += 1
        while current_node._next is not None:
          current_node = current_node._next
          # Count each existing node in center list
          self._total += 1
        # Point tail of center list to larger list's head
        current_node._next = larger._quick_sort(sort_by)._head
        # Move to tail of larger list
        while current_node._next is not None:
          current_node = current_node._next
          # Count each existing node in larger list
          self._total += 1
        return self
      # If smaller is not empty, start from smaller head and move to smaller tail
      else:
        current_node = self._head
        self._total += 1
        while current_node._next is not None:
          current_node = current_node._next
          # Count each existing node in smaller list
          self._total += 1
        # Point tail of smaller list to center list's head
        current_node._next = center._head
        # Move to tail of center list
        while current_node._next is not None:
          current_node = current_node._next
          # Count each existing node in center list
          self._total += 1
        # Point tail of center list to larger list's head
        current_node._next = larger._quick_sort(sort_by)._head
        # Move to tail of larger list
        while current_node._next is not None:
          current_node = current_node._next
          # Count each existing node in center list
          self._total += 1
        return self
    
  # Outer sort function  
  def sort(self, sort_type, sort_by = "date-time"):
    # Perform sort on clone of linked list to avoid mutating the original

    # Helper function to create clone of existing linked list 
    def _clone_linked_list(src):
      # Initial clone as empty linked list
      clone = LinkedList()
      original_node = src._head
      clone_tail = None
      while original_node is not None:
        clone_node = LinkedListNode(original_node._value)
        if clone_tail is None:
          clone._head = clone_node
        else:
          clone_tail._next = clone_node
        clone_tail = clone_node
        clone._total += 1
        original_node = original_node._next
      return clone

    # Create clone of existing linked list
    clone_linked_list = _clone_linked_list(self)

    # Insertion sort
    if sort_type == "insertion":
      return clone_linked_list._insertion_sort(sort_by)
    # Merge sort
    elif sort_type == "merge":
      return clone_linked_list._merge_sort(sort_by)
    # Quick sort
    elif sort_type == "quick":
      return clone_linked_list._quick_sort(sort_by)
    # Invalid sort
    else:
      return "Error: sort_type must be \"insertion\", \"merge\", or \"quick\"."
  
  # Linear search: Works for sorted and unsorted linked lists
  def linear_search(self, id):
    # If head is None, stop and return error
    if self._head is None:
      return None
    # Start from head and move on next nodes. If a node's event id matches the given id, return the node's event
    current_node = self._head
    while current_node is not None:
      if current_node._value["id"] == id:
        return current_node._value
      current_node = current_node._next
    # If event is not found, return None
    return None
  
  # Binary search: Only works on sorted linked list
  def binary_search(self, id):
    # If head is None, stop and return error
    if self._head is None:
      return None
    # First, get a sorted copy of the list by event ID using merge sort to perform search on
    sorted_list = self.sort(sort_type = "merge", sort_by = "id")
    # Set linked list movement range parameters
    start = sorted_list._head
    end = None
    slow = start
    # While a range exists from start to end, increment slow by 1 step each time and fast by 2 steps each time such that fast reaches the end and slow reached the midpoint
    while start != end:
      slow = start
      fast = start
      while fast != end and fast._next != end:
        slow = slow._next
        fast = fast._next._next
      mid = slow
      # If midpoint node's event ID matches given ID, return midpoint event
      if mid._value["id"] == id:
        return mid._value
      # If midpoint node's event ID is smaller than the given ID, adjust range such that the start is now the node after midpoint
      elif mid._value["id"] < id:
        start = mid._next
      # If midpoint node's event ID is greater than the given ID, adjust range such that the end is now the midpoint
      else:
        end = mid
    # If range shrinks to zero and still no id match, return None
    return None

  # Conflict detection - Check if two events overlap
  def conflict_detect(self, new_event):
    # Start from head and move on next nodes. If a node's event id matches the given id, return the node's event
    current_node = self._head
    while current_node is not None:
      # Mark as conflict if new event's location matches another existing event and if new event's date-time period overlaps with another event's date-time period
      # Overlap occurs when 1. new event end > current event start and new event start < current event end or 2. new event start < current event end and new event end > current event start
      if current_node._value["location"] == new_event["location"] and ((get_event_dt_end(new_event) > get_event_dt_start(current_node._value) and get_event_dt_start(new_event) < get_event_dt_end(current_node._value)) or (get_event_dt_start(new_event) < get_event_dt_end(current_node._value) and get_event_dt_end(new_event) > get_event_dt_start(current_node._value))):
        return True
      current_node = current_node._next
    # If no conflict found, return False
    return False

  # Insert method
  def insert(self, new_event):
    # Assuming array is unsorted, use linear_search to check if event id already exists. If yes, return error and stop
    if self.linear_search(new_event["id"]):
      return "Error: Event ID already exists."
    # If there is a conflict with another event, print error and stop
    elif self.conflict_detect(new_event) == True:
      return "Error: There is already another existing event scheduled for the same date, time, and location."
    # Proceed to insert new event if there is no conflict
    else:
      # Implement new campus event as a linked list node
      new_node = LinkedListNode(new_event)
      # If head node is None, make new_node the head
      if self._head is None:
        self._head = new_node
      else:
        # Start from head node, move sequentially until tail node where next attr is None
        current_node = self._head
        while current_node._next:
          current_node = current_node._next
        # Point tail node to new node
        current_node._next = new_node
      self._total += 1
      return f"Event ID {new_event["id"]}: \"{new_event["title"]}\" has been inserted into the linked list."

  # Delete method: Delete by event ID
  def delete(self, event_id):
    # If there are no nodes in linked list, print error and stop
    if self._head is None:
      return "Error: There are no events in the linked list to delete."
    # If event ID matches head node
    if self._head._value["id"] == event_id:
      # Save title of event to be deleted
      del_event_title = self._head._value["title"]
      # Set next node as new head
      self._head = self._head._next
      self._total -= 1
      return f"Event ID {event_id}: \"{del_event_title}\" has been deleted from the linked list."
    # Check next nodes after head for match in event ID
    current_node = self._head
    while current_node._next is not None:
      # If event ID of the next node matches
      if current_node._next._value["id"] == event_id:
        # Save title of event to be deleted
        del_event_title = current_node._next._value["title"]
        # Delete next node by pointing current node to the node after next
        current_node._next = current_node._next._next
        self._total -= 1
        return f"Event ID {event_id}: \"{del_event_title}\" has been deleted from the linked list."
      # Move to next node if current node does not match
      else:
        current_node = current_node._next
    # If no matches found at the end of linked list, print error
    return f"Error: Event ID {event_id} does not exist in the linked list."

  # Search-by-id method
  def search_by_id(self, event_id, search_method = "linear"):
    # Linear search
    if search_method == "linear":
      # Save the result found
      if self.linear_search(event_id) is not None:
        event = self.linear_search(event_id)
      # If result is None, print error: Event ID not found.
      else:
        return "Error: Event ID not found."
    # Binary search - array must already be sorted by event ID
    elif search_method == "binary":
      # Save the result found
      if self.binary_search(event_id) is not None:
        event = self.binary_search(event_id)
      # If result is None, print error: Event ID not found.
      else:
        return "Error: Event ID not found."
    # If an invalid search method is provided, print error and stop
    else:
      return "Error: search_method must be \"linear\" or \"binary\"."
    # Return the result event's details
    return f"Event ID {event_id} pertains to:\nTitle: {event["title"]}\nDate: {event["date"]}\nStart Time: {event["time_start"]}\nEnd Time: {event["time_end"]}\nLocation: {event["location"]}"
  
  # List all method
  def list_all(self):
    # If there are no events, i.e., the head node is None, print error
    if self._head is None:
      return "There are no events."
    else:
      # Print each event's details
      print_str = ""
      # Start from head, move through list until tail node
      current_node = self._head
      while current_node is not None:
        print_str += "Event ID: {0}\nTitle: {1}\nDate: {2}\nStart Time: {3}\nEnd Time: {4}\nLocation: {5}\n\n".format(current_node._value["id"], current_node._value["title"], current_node._value["date"], current_node._value["time_start"], current_node._value["time_end"], current_node._value["location"])
        current_node = current_node._next 
      return(print_str)