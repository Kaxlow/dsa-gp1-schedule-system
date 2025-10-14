def insertionSortArrayList (eventsList):
    for i in range(1, len(eventsList)):
        key = eventsList[i]
        key_date = datetime.strptime(key["date"] + " " + key["start_time"], "%Y-%m-%d %H:%M")
        j = i - 1
        # Move elements of eventsList[0..i-1], that have greater date + start_time combination than key to one position ahead
        # of their current position
        while j >= 0:
            j_date = datetime.strptime(eventsList[j]["date"] + " " + eventsList[j]["start_time"], "%Y-%m-%d %H:%M")
            if j_date > key_date:
                eventsList[j + 1] = eventsList[j]
                j -= 1
            else:
                break
        eventsList[j + 1] = current
