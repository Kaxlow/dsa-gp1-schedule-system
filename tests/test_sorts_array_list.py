# tests/test_sorts_array_list.py
from src.sorts_array_list import insertion_sort_array, merge_sort_array, quick_sort_array
import random

def make_event(i, date="2025-10-01", time="09:00"):
    return {"id": i, "title": f"Event{i}", "date": date, "time": time, "location": "Hall"}

def test_insertion_sort_simple():
    arr = [
        make_event(1, "2025-12-01", "10:00"),
        make_event(2, "2025-10-01", "09:00"),
        make_event(3, "2025-11-01", "08:00"),
    ]
    insertion_sort_array(arr)
    keys = [ (e["date"], e["time"]) for e in arr ]
    assert keys == sorted(keys)

def test_merge_sort_stability_and_edge_cases():
    # same date+time but different id: preserve relative order (stable mergesort)
    arr = [
        {"id":1,"title":"A","date":"2025-10-10","time":"10:00","location":"X"},
        {"id":2,"title":"B","date":"2025-10-10","time":"10:00","location":"Y"},
        {"id":3,"title":"C","date":"2025-10-09","time":"09:00","location":"Z"},
    ]
    sorted_arr = merge_sort_array(arr)
    assert [e["id"] for e in sorted_arr] == [3,1,2]  # 1 before 2 preserved

def test_quick_sort_random():
    # random dates among 5 days
    base_days = [f"2025-10-{day:02d}" for day in range(1,6)]
    arr = []
    for i in range(50):
        d = random.choice(base_days)
        t = f"{random.randint(0,23):02d}:{random.randint(0,59):02d}"
        arr.append({"id":i, "title":f"E{i}", "date":d, "time":t, "location":"L"})
    sorted_q = quick_sort_array(arr)
    keys = [ (e["date"], e["time"]) for e in sorted_q ]
    assert keys == sorted(keys)
