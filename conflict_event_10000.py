import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import time
import random
from conflict import detect_conflicts   

# create a simple list of events
def generate_event(n):
    events = []
    for i in range(n):
        start_hour = (i * 2) % 24     # each event starts 2 hours apart
        end_hour = (start_hour + 1) % 24 ## each event lasts one hour 
        events += [{
            "id": i,
            "title": f"Event {i}",
            "date": "2025-01-01",
            "time": f"{start_hour:02d}:00",
            "end":  f"{end_hour:02d}:00"
        }]
    return events

# generate 10 000 events
events = generate_event(10000)

print("Running conflict detection on 10,000 events...")
start = time.time()
conflicts = detect_conflicts(events)
end = time.time()

print(f"Total events: {len(events)}")
print(f"Conflicts found: {len(conflicts)}")
print(f"Runtime: {(end - start):.3f} seconds")
