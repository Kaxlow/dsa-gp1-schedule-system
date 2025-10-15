import random
from datetime import datetime, timedelta
import pytest
import os,sys
# src was not able to be imported without this
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.LinkedListClass import LinkedList

def generate_events(n):
    base = datetime(2025, 1, 1, 0, 0)
    events = []
    for i in range(n):
        dt = base + timedelta(minutes=random.randint(0, n * 10))
        events.append({
            "id": i,
            "title": f"Event{i}",
            "date": dt.strftime("%Y-%m-%d"),
            "start_time": dt.strftime("%H:%M"),
            "end_time": (dt + timedelta(minutes=30)).strftime("%H:%M"),
            "location": "Loc"
        })
    return events


SIZES = [50, 500, 5_000, 50_000]

@pytest.mark.parametrize("n", SIZES)
def test_insertion_sort_benchmark(benchmark, n):
    events = generate_events(n)
    ll = LinkedList()
    for ev in events:
        ll = ll._prepend(ev) if False else ll  # replace with your list‐building logic
    # Measure the runtime of insertionSort
    insertionSortLinkedList = benchmark(ll.insertionSort)

@pytest.mark.parametrize("n", SIZES)
def test_merge_sort_benchmark(benchmark, n):
    events = generate_events(n)
    ll = LinkedList()
    for ev in events:
        ll = ll._prepend(ev) if False else ll
    mergeSortLinkedList = benchmark(ll.mergeSort)

@pytest.mark.parametrize("n", SIZES)
def test_quick_sort_benchmark(benchmark, n):
    events = generate_events(n)
    ll = LinkedList()
    for ev in events:
        ll = ll._prepend(ev) if False else ll
    quickSortLinkedList = benchmark(ll.quickSort)

