import copy
from datetime import datetime
class ArrayList :
    def __init__(self):
        # Use list of n Nones to represent initial array with capacity of n
        self._size = 0
        self._capacity = 1
        self._collection = [None] * self._capacity
    # we need methods that can help with indexing and performing operations on the array
    #use this method to extract event from a particular index
    #use this meh

    def insertionSortArrayList(self):
        #taking a copy of the list so it does not change the original one
        sortedEvents = copy.deepcopy(self.events)
        for curr in range(1, len(sortedEvents)):
            #storing the current event in i to compare it with the previous events
            currEvent = sortedEvents[curr]
            currEventDate = datetime.strptime(currEvent["date"] + " " + currEvent["start_time"], "%Y-%m-%d %H:%M")
            #used to loop over the previous events and replace them if they are starting after the current event
            prev = curr - 1
            # Move elements of eventsList[0..i-1], that have greater date + start_time combination than key to one position ahead
            # of their current position
            while prev >= 0:
                prevEventDate = datetime.strptime(sortedEvents[prev]["date"] + " " + sortedEvents[prev]["start_time"], "%Y-%m-%d %H:%M")
                if prevEventDate > currEventDate:
                    #checking previous and current event dates and start_times
                    #print("Swapping ", sortedEvents[prev], " and ", currEvent)
                    sortedEvents[prev + 1] = sortedEvents[prev]
                    prev -= 1
                else:
                    break
            sortedEvents[prev + 1] = currEvent
        return sortedEvents
    
    def merge(left,right):
        #creating a new list to store the merged events after sorting them
        totalSize = len(left) + len(right)
        mergedEvents = [None] * totalSize
        leftIndex = 0
        rightIndex = 0
        idx = 0
        #checking for the date + start_time to see the order of the events
        while leftIndex < len(left) and rightIndex < len(right):
            leftEventDate = datetime.strptime(left[leftIndex]["date"] + " " + left[leftIndex]["start_time"], "%Y-%m-%d %H:%M")
            rightEventDate = datetime.strptime(right[rightIndex]["date"] + " " + right[rightIndex]["start_time"], "%Y-%m-%d %H:%M")
            if leftEventDate <= rightEventDate:
                mergedEvents[idx] = left[leftIndex]
                leftIndex += 1
            else:
                mergedEvents[idx] = right[rightIndex]
                rightIndex += 1
            idx += 1
            
        while leftIndex < len(left):
            mergedEvents[idx] = left[leftIndex]
            leftIndex += 1
            idx += 1

        while rightIndex < len(right):
            mergedEvents[idx] = right[rightIndex]
            rightIndex += 1
            idx += 1
        return mergedEvents

    def mergeSortArrayList(self):
        sortedEvents = copy.deepcopy(self.events)
        return self.mergeSort(sortedEvents)
    
    def mergeSort(self, splitArray):
        if len(splitArray) <= 1:
            return splitArray
        mid = len(splitArray) // 2
        left = self.mergeSort(splitArray[:mid])
        right = self.mergeSort(splitArray[mid:])
        return self.merge(left, right)

    def quicksortArrayList(self):
        sortedEvents = copy.deepcopy(self.events)
        return self.quickSort(sortedEvents)

    def quickSort(self, eventArray):
        n = len(eventArray)
        if n <= 1:
            return eventArray

        pivot = eventArray[n // 2]
        pivot_date = datetime.strptime(pivot["date"] + " " + pivot["start_time"], "%Y-%m-%d %H:%M")

        less = [None] * n, less_count = 0
        equal = [None] * n, equal_count = 0
        greater = [None] * n, greater_count = 0

        for i in range(n):
            event = eventArray[i]
            event_date = datetime.strptime(event["date"] + " " + event["start_time"], "%Y-%m-%d %H:%M")

            if event_date < pivot_date:
                less[less_count] = event
                less_count += 1
            elif event_date == pivot_date:
                equal[equal_count] = event
                equal_count += 1
            else:
                greater[greater_count] = event
                greater_count += 1

        sorted_less = self.quickSort(less[:less_count]) if less_count > 0 else []
        sorted_greater = self.quickSort(greater[:greater_count]) if greater_count > 0 else []

        sortedEvents_len = less_count + equal_count + greater_count
        sortedEvents = [None] * sortedEvents_len

        idx = 0
        for i in range(len(sorted_less)):
            sortedEvents[idx] = sorted_less[i]
            idx += 1
        for i in range(equal_count):
            sortedEvents[idx] = equal[i]
            idx += 1
        for i in range(len(sorted_greater)):
            sortedEvents[idx] = sorted_greater[i]
            idx += 1

        return sortedEvents





    



    