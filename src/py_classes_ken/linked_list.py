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

  # Define helper function to set sort attribute for running sort algorithms
  def _set_sort_attr(self, event, sort_by):
    if sort_by == "date_time":
      return get_event_dt_start(event)
    elif sort_by == "id":
      return event["id"]
    else:
      return "Error: Must sort by \"date_time\" or \"id\"."

  # Insertion sort. By default, sort by event date and time.
  def insertion_sort(self, sort_by = "date_time"):
    # Starting from second-left element, take each element and insert into sorted array
    for outer in range(1, self._total):
      # Save outer element to insert into sorted array. Start from head and move to outer node
      current_node = self._head
      for i in range(outer):
        current_node = current_node.next
      outer_node = current_node
      # Mark boundary between sorted and unsorted sections
      inner = outer - 1
      # Save inner element
      current_node = self._head
      for i in range(inner):
        current_node = current_node.next
      inner_node = current_node
      # While new element's sort-by attribute is smaller than sorted array element's corresponding attribute, shift sorted array's element to the right
      while inner > 0 and self._set_sort_attr(outer_node._value, sort_by) < self._set_sort_attr(inner_node._value, sort_by):
        # Find next inner element
        inner -= 1
        current_node = self._head
        for i in range(inner):
          current_node = current_node.next
        inner_node = current_node
      # Insert element when the right shifts stop
      # First, move to node before outer node
      current_node = self._head
      for i in range(outer - 1):
        current_node = current_node.next
        # Point the node before outer node to the node after outer node
        current_node.next = current_node.next.next
      # Next, move to node before latest inner node
      current_node = self._head
      for i in range(inner - 1):
        current_node = current_node.next
      # Point node before inner node to outer node
      current_node.next = outer_node
      # Then point outer node to inner node
      outer_node.next = inner_node
    return self
  
  # Merge sort. By default, sort by event date and time
  def merge_sort(self, sort_by = "date_time"):
    # If linked list has multiple elements, split into left and right lists recursively
    # If linked list is left with one element, it is unchanged and returns as sorted_arr
    if self._total > 1:
      # Prepare left list from original list
      left_list = self
      # Start from head and move to node before midpoint
      current_node = self._head
      for i in range(list_len // 2):
        current_node = current_node.next
      # Create right list as a new linked list starting from node after midpoint node and ending at tail node
      right_list = LinkedList(current_node.next)
      # Finalize left list by truncating at midpoint node
      current_node.next = None
      merge_sort(left_list, sort_by)
      merge_sort(right_list, sort_by)
      # Merge splits lists in sort order
      # Initialize sorted linked list
      sorted_linked_list = LinkedList(None)
      # While both left_list and right_list still have un-merged nodes
      while left_list is not None and right_list is not None:
        # If left_list's head's sort-by attribute <= right_list's head's sort-by attribute, left_list's head becomes the next node in sorted_linked_list
        if self._set_sort_attr(left_list._head._value, sort_by) <= self._set_sort_attr(right_list._head._value, sort_by):
          sorted_linked_list._head = left_list._head
          # Make left_list's next node the new head
          left_list._head = left_list._head.next
        # Else, right_list's head becomes the next node in sorted_linked_list
        else: 
          sorted_linked_list._head = right_list._head
          # Make right_list's next node the new head
          right_list._head = right_list._head.next
      # While only left_list has un-merged nodes
      while left_list is not None:
        sorted_linked_list._head = left_list._head
        left_list._head = left_list._head.next
      # While only right_arr has un-merged elements
      while right_list is not None:
        sorted_linked_list._head = right_list._head
        right_list._head = right_list._head.next
      return sorted_linked_list
    
  # Quick sort. By default, sort by event date and time
  def quick_sort(self, sort_by = "date_time"):
    # Base case: return linked list unchanged if there's zero or one element
    if self._total <= 1:
      return self
    else:
      # Select node at median position as pivot
      # Start from head and move to node at median position
      current_node = self._head
      for i in range(self._total // 2):
        current_node = current_node.next
      pivot_node = current_node
      # Move each element into sub-lists by comparing against pivot
      smaller = LinkedList(None)
      center = LinkedList(None)
      larger = LinkedList(None)
      # Compare each node event's sort-by attribute against the pivot node event's sort-by attribute, starting from head
      while self._head is not None:
        current_node = self._head
        # Remove pointer from current_node to be inserted into sub-lists
        current_node.next = None
        # Update head to next node in original list
        self._head = self._head.next
        # If event's sort-by attribute is smaller than pivot event's sort-by attribute, move node to smaller list
        if self._set_sort_attr(current_node._value, sort_by) < self._set_sort_attr(pivot_node._value, sort_by):
          if smaller._head is None:
            smaller._head = current_node
          else:
            # Move to end of smaller list, then append current_node
            smaller_current_node = smaller._head
            while smaller_current_node.next is not None:
              smaller_current_node = smaller_current_node.next
            smaller_current_node.next = current_node
        # If event's sort-by attribute is larger than pivot event's sort-by attribute, move node to larger list
        elif self._set_sort_attr(current_node._value, sort_by) > self._set_sort_attr(pivot_node._value, sort_by):
          if larger._head is None:
            larger._head = current_node
          else:
            # Move to end of larger list, then append current_node
            larger_current_node = larger._head
            while larger_current_node.next is not None:
              larger_current_node = larger_current_node.next
            larger_current_node.next = current_node
        # If event's sort-by attribute is equal to pivot event's sort-by attribute, move node to center list
        else:
          center._head = current_node
      # Recursively split sub-lists around new pivots until no longer possible
      # Join split arrays in order of smaller, center, larger
      rejoined_list = quick_sort(smaller, sort_by)._head
      rejoined_node = rejoined_list._head
      # Move to tail of smaller list
      while rejoined_node.next is not None:
        rejoined_node = rejoined_node.next
      # Point tail of smaller list to center list's head
      rejoined_node.next = center._head
      # Move to tail of center list
      while rejoined_node.next is not None:
        rejoined_node = rejoined_node.next
      # Point tail of center list to larger list's head
      rejoined_node.next = quick_sort(larger, sort_by)._head
      return rejoined_list
  
  # Linear search: Works for sorted and unsorted linked lists
  def linear_search(self, id):
    # Start from head and move on next nodes. If a node's event id matches the given id, return the node's event
    current_node = self._head
    while current_node is not None:
      if current_node._value["id"] == id:
        return current_node._value
    # If event is not found, return None
    return None
  
  # Binary search: Only works on sorted linked list
  def binary_search(self, id):
    # First, sort the array by event ID using merge sort
    self.merge_sort(sort_by = "id")
    # Set linked list movement range parameters
    start = self._head
    # steps_max = number of steps from head to tail nodes
    steps_max = self._total - 1
    steps_to_mid = range(steps_max // 2)
    # While search range has multiple nodes, i.e., start and mid have not coincided yet
    while steps_max > 0:
      # Move from start to midpoint
      current_node = start
      for i in steps_to_mid:
        current_node = current_node.next
      # Mark the midpoint
      mid = current_node
      # If id matches the event at midpoint, return the event
      if id == mid._value["id"]:
        return mid._value
      # If id is greater than midpoint event's id, search upper half starting from node after midpoint
      elif id > mid._value["id"]:
        start = mid.next
        # Update linked list search range to upper half
        steps_max = steps_max - steps_to_mid - 1
        steps_to_mid = range(steps_max // 2)
      # If id is smaller than midpoint event's id, search lower half, starting from the same start node as before
      else:
        # Update linked list search range to lower half
        steps_max = steps_to_mid
        steps_to_mid = range(steps_max // 2)
    # When there is one node left in search range and its event id is a match, return the event, else return None
    if start._value is None:
      return None
    elif start._value["id"] == id:
      return start._value
    else:
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
      # Start from head node, move sequentially until tail node where next attr is None
      current_node = self._head
      while current_node is not None:
        current_node = current_node.next
      # Point tail node to new node
      current_node = new_node
      self._total += 1
      print(f"Event ID {new_event["id"]}: \"{new_event["title"]}\" has been inserted into the linked list.")

  # Delete method: Delete by event ID
  def delete(self, event_id):
    # If there are no nodes in linked list, print error and stop
    if self_.head is None:
      print("Error: There are no events in the linked list to delete.")
      return
    # If event ID matches head node
    if self._head._value["id"] == event_id:
      # Save title of event to be deleted
      del_event_title = self._head._value["title"]
      # Set next node as new head
      self._head = self._head._next
      print(f"Event ID {event_id}: \"{del_event_title}\" has been deleted from the linked list.")
      return
    # Check next nodes after head for match in event ID
    current_node = self._head
    while current_node.next is not None:
      # If event ID of the next node matches
      if current_node._next._value["id"] == event_id:
        # Save title of event to be deleted
        del_event_title = current_node._next._value["title"]
        # Delete next node by pointing current node to the node after next
        current_node._next = current_node._next._next
        self._total -= 1
        print(f"Event ID {event_id}: \"{del_event_title}\" has been deleted from the linked list.")
        return
      # Move to next node if current node does not match
      else:
        current_node = current_node.next
    # If no matches found at the end of linked list, print error
    print("Error: Event ID not found in linked list.")

  # Search-by-id method
  def search_by_id(self, event_id, search_method = "linear"):
    # Linear search
    if search_method == "linear":
      # Save the result found
      if self.linear_search(event_id) is not None:
        event = self.linear_search(event_id)
      # If result is None, print error: Event ID not found.
      else:
        print("Error: Campus Event ID not found.") 
        return
    # Binary search - array must already be sorted by event ID
    elif search_method == "binary":
      # Save the result found
      if self.binary_search(event_id) is not None:
        event = self.binary_search(event_id)
      # If result is None, print error: Event ID not found.
      else:
        print("Error: Campus Event ID not found.") 
        return
    # If an invalid search method is provided, print error and stop
    else:
      print("Error: search_method must be \"linear\" or \"binary\".")
      return
    # Print the result event's details
    print(f"Campus Event ID {event_id} pertains to:\nTitle: {event["title"]}\nDate: {event["date"]}\nStart Time: {event["time_start"]}\nEnd Time: {event["time_end"]}\nLocation: {event["location"]}")
    return
  
  # List all method
  def list_all(self):
    # If there are no events, i.e., the head node is None, print error
    if self._head is None:
      print("Error: No existing events.")
    else:
      # Print each event's details
      print_str = ""
      # Start from head, move through list until tail node
      current_node = self._head
      while current_node is not None:
        print_str += "Event ID: {0}\nTitle: {1}\nDate: {2}\nStart Time: {3}\nEnd Time: {4}\nLocation: {5}\n\n".format(current_node._value["id"], current_node._value["title"], current_node._value["date"], current_node._value["time_start"], current_node._value["time_end"], current_node._value["location"])
        current_node = current_node.next 
      print(print_str)