def detect_conflicts(events):
  
    
    n = len(events) ## count the number  of events
    for i in range(n - 1):
        for j in range(n - i - 1):  # sort events by date and time
            if (events[j]["date"], events[j]["time"]) > (events[j + 1]["date"], events[j + 1]["time"]): ## Bubble sort to manually sort the events
                events[j], events[j + 1] = events[j + 1], events[j] ## first sort event by date and then by time

   
    conflicts = [None] * n ## creating a list of fixed size n
    conflict_count = 0

    # Compare each event with its next one
    for i in range(n - 1):
        e1 = events[i]
        e2 = events[i + 1]

      
        if e1["date"] == e2["date"] and e1["end"] > e2["time"]: ## does e1 and after e2 start ??
            conflicts[conflict_count] = (e1["id"], e2["id"])
            conflict_count += 1

   
    result = []
    for i in range(conflict_count):
        result += [conflicts[i]]  
    return result

