# Import modules
from datetime import datetime, time
from .utils import get_event_dt_start, get_event_dt_end

# Define class for dynamic array
# None should only exist in excess spaces on the right of the array
class DynamicArray:
  def __init__(self):
    # Use list of n Nones to represent initial array with capacity of n
    self._size = 0
    self._capacity = 1
    self._collection = [None] * self._capacity

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

  # Insertion sort
  def _insertion_sort(self, arr, sort_by):
    # Starting from second-left element, take each element and insert into sorted array
    for outer in range(1, len(arr)):
      # Save element to insert into sorted array
      temp = arr[outer] 
      # Mark boundary between sorted and unsorted sections
      inner = outer
      # While new element's sort-by attribute is smaller than sorted array element's corresponding attribute, shift sorted array's element to the right
      while inner > 0 and self._set_sort_attr(temp, sort_by) < self._set_sort_attr(arr[inner - 1], sort_by):
        arr[inner] = arr[inner - 1]
        inner -= 1
      # Insert element when the right shifts stop
      arr[inner] = temp
    return arr

  # Merge sort
  def _merge_sort(self, arr, sort_by):
    # If array has multiple elements, split into two recursively
    # If array is left with one element, it is unchanged and returns as is
    if len(arr) > 1:
      left_arr = arr[:(len(arr) // 2)]
      right_arr = arr[(len(arr) // 2):]
      self._merge_sort(left_arr, sort_by)
      self._merge_sort(right_arr, sort_by)
      # Merge left_arr and right_arr back into arr in sorted order
      # Initialize arr indices for left, right, and merged arrays
      i = j = k = 0
      # While both left_arr and right_arr still have un-merged elements
      while i < len(left_arr) and j < len(right_arr):
        # If first element of left_arr's sort-by attribute <= first element of right_arr's sort-by attribute, move first element of left_arr into arr
        if self._set_sort_attr(left_arr[i], sort_by) <= self._set_sort_attr(right_arr[j], sort_by):
          arr[k] = left_arr[i]
          i += 1
          k += 1
        # Else move the first element of right_arr into arr
        else:
          arr[k] = right_arr[j]
          j += 1
          k += 1
      # While only left_arr has un-merged elements
      while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
      # While only right_arr has un-merged elements
      while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1
      return arr
    
  # Quick sort 
  def _quick_sort(self, arr, sort_by):
    # Base case: return array unchanged if there's zero or one element
    if len(arr) <= 1:
      return arr
    else:
      # Select element with median key as pivot
      pivot = arr[len(arr) // 2]
      # Move each element into corresponding sub-arrays by comparing the event's sort-by attribute against the pivot event's sort-by attribute
      smaller = []
      center = []
      larger = []
      for ele in arr:
        if self._set_sort_attr(ele, sort_by) < self._set_sort_attr(pivot, sort_by):
          smaller += [ele]
        elif self._set_sort_attr(ele, sort_by) > self._set_sort_attr(pivot, sort_by):
          larger += [ele]
        else:
          center += [ele]
      # Recursively split sub-arrays around new pivots until no longer possible
      # Join split arrays in order
      arr = self._quick_sort(smaller, sort_by) + center + self._quick_sort(larger, sort_by)
      return arr

  # Outer sort function  
  def sort(self, sort_type, sort_by = "date-time"):
    # Operate on a copy of self._collection
    arr = self._collection
    # First, remove trailing Nones from array before sort, counting the number of Nones removed
    none_count = 0
    while arr[-1] is None:
      arr = arr[:(len(arr) - 1)]
      none_count += 1
    # The sort functions return a sorted py list for self._collection
    # Insertion sort
    if sort_type == "insertion":
      arr = self._insertion_sort(arr, sort_by)
    # Merge sort
    elif sort_type == "merge":
      arr = self._merge_sort(arr, sort_by)
    # Quick sort
    elif sort_type == "quick":
      arr = self._quick_sort(arr, sort_by)
    # Invalid sort
    else:
      return "Error: sort_type must be \"insertion\", \"merge\", or \"quick\"."
    # Append previously dropped Nones back to sorted array
    for i in range(none_count):
      arr.append(None)
    # Update self._collection to the sorted array with Nones added back
    self._collection = arr
    return self
    
  # Linear search: Works for sorted and unsorted arrays
  def linear_search(self, id):
    # Find event whose id matches given id, then return event
    for event in self._collection:
      if event is not None and event["id"] == id:
        return event
    # If event is not found, return None
    return None

  # Binary search: Only works on sorted arrays
  def binary_search(self, id):
    # First, sort the array by event ID using merge sort
    self.sort(sort_type = "merge", sort_by = "id")
    # Make a copy of the array in self._collection to run the search, dropping any Nones
    arr = self._collection
    while arr[-1] is None:
      arr = arr[:(len(arr) - 1)]
    # Check midpoint of array if array has multiple elements
    while len(arr) > 1:
      # If id matches the event at midpoint, return the event
      if id == arr[len(arr) // 2]["id"]:
        return arr[len(arr) // 2]
      # If id is greater than midpoint event's id, repeat check on the upper half of the array
      elif id > arr[len(arr) // 2]["id"]:
        arr = arr[len(arr) // 2:]
      # If id is smaller than midpoint event's id, repeat check on lower half of array
      else:
        arr = arr[:len(arr) // 2]
    # When there is one element left in array, check if it matches the given id
    if arr[0]["id"] == id:
      return arr[0]
    # If event is not found, return None
    else:
      return None

  # Conflict detection - Check if two events overlap
  def conflict_detect(self, new_event):
    for i in range(self._size):
      event = self._collection[i]
      # Mark as conflict if new event's location matches another existing event and if new event's date-time period overlaps with another event's date-time period
      # Overlap occurs when 1. new event end > current event start and new event start < current event end or 2. new event start < current event end and new event end > current event start
      if event is not None and event["location"] == new_event["location"] and ((get_event_dt_end(new_event) > get_event_dt_start(event) and get_event_dt_start(new_event) < get_event_dt_end(event)) or (get_event_dt_start(new_event) < get_event_dt_end(event) and get_event_dt_end(new_event) > get_event_dt_start(event))):
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
      # If array is at capacity, increase capacity by 1
      if self._size == self._capacity:
        self._capacity += 1
        self._collection.append(None)
        print(f"The array's capacity has been increased to {self._capacity}.")
      # Overwrite first None element from the left with new event
      for i in range(len(self._collection)):
        if self._collection[i] is None:
          self._collection[i] = new_event
          break
      self._size += 1
      return f"Event ID {new_event["id"]}: \"{new_event["title"]}\" has been inserted into the array."

  # Delete method: Delete event by ID
  def delete(self, event_id):
    # Find event in array
    for i in range(self._capacity):
      # Ignore Nones in array
      if self._collection[i] is None:
        continue
      if self._collection[i]["id"] == event_id:
        # Save title of the event to be deleted
        del_event_title = self._collection[i]["title"]
        # Delete event and shift the next elements left
        for j in range(i, self._size - 1):
          self._collection[j] = self._collection[j + 1]
        # Space previously occupied by last element becomes None
        self._collection[self._size - 1] = None
        self._size -= 1
        return f"Event ID {event_id}: \"{del_event_title}\" has been deleted from the array."
        
    # If event is not in array, print error and stop
    return f"Error: Event ID {event_id} does not exist in array."

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
    # Print the result event's details
    return f"Event ID {event_id} pertains to:\nTitle: {event["title"]}\nDate: {event["date"]}\nStart Time: {event["time_start"]}\nEnd Time: {event["time_end"]}\nLocation: {event["location"]}"  

  # List all method
  def list_all(self):
    # If there are no events, i.e., the first element is None, print error
    if self._collection[0] is None:
      return "There are no events."
    else:
      # Print each event's details
      print_str = ""
      for event in self._collection:
        if event is not None:
          print_str += "Event ID: {0}\nTitle: {1}\nDate: {2}\nStart Time: {3}\nEnd Time: {4}\nLocation: {5}\n\n".format(event["id"], event["title"], event["date"], event["time_start"], event["time_end"], event["location"])
      return print_str