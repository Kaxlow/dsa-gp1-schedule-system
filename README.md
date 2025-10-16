# Schedule System

This Python package runs a schedule system that stores and operates on events in the following format:

```
Event = {
  "id": int,           # unique   
  "title": str,
  "date": str,         # format YYYY-MM-DD
  "time_start": str,   # format HH:MM
  "time_end": str,     # format HH:MM
  "location": str
  }
```
The system can run using either a dynamic array or a linked list on the back-end.

In the `src` folder, the `py_classes_ken` package contains the following source files:
- `utils.py` - contains functions used throughout the package
- `dynamic_array.py` - contains definition of the `DynamicArray()` class and its associated methods
- `linked_list.py` - contains definition of the `LinkedList()` class and its associated methods

The methods defined for the `DynamicArray()` and `LinkedList()` classes are:
- `sort` which can run either the insertion sort, merge sort, or quick sort algorithm as specified in the function's `sort_type` argument
- `linear_search`
- `binary_search`
- `conflict_detect`
- `insert`
- `delete`
- `search_by_id` which runs with either `linear_search` or `binary_search`
- `list_all`

The `tests` folder contain scripts for pytest to assert that the code works as expected.

## Setup and Execution
The `py_classes_ken` package can be installed in a python environment. After installing the package, it and any of the modules within can be called in Python code.

## Team Roles
Ken worked on the sort, search, and conflict detection algorithms and the supporting methods `insert`, `delete`, `search_by_id` and `list_all` for both the dynamic array and linked list structures. Ken ran the sort, search, and conflict detection algorithms on different sample sizes of events and documented the time taken in each scenario, then plotted charts showing the differences in time taken.
Chushmitha worked on the sort methods for both the dynamic array and linked list structures, complexity of operations, and suggested optimizations.
Himanshu worked on the conflict detection and search methods for the dynamic array class, as well as complexity of operations
Abhirama worked on on the sort, search, and conflict detection algorithms and the supporting methods `insert`, `delete`, `search_by_id` and `list_all` for both the dynamic array and linked list structures. Abhirama also wrote about the system's scalability using both the dynamic array and linked list structures, performing an analysis of memory usage and suggesting improvements to conflict detection.