# Import modules
import time
import pytest
import json

# Import LinkedList class
from py_classes_ken import linked_list

# Create an instance of LinkedList
ll = linked_list.LinkedList()

# Insert 5 events
new_events = json.load(open("tests/random_events_5.json"))
for event in new_events:
  ll.insert(event)