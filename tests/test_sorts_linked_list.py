# tests/test_sorts_linked.py
from src.sorts_linked_list import insertion_sort_linked_list, merge_sort_linked_list, quick_sort_linked_list
from src.linked_list import LinkedList

def make_event(i, date="2025-10-01", time="09:00"):
    return {"id": i, "title": f"Event{i}", "date": date, "time": time, "location": "Hall"}

def list_to_keys(ll):
    return [(e["date"], e["time"]) for e in ll.list_all()]

def test_insertion_sort_linked_list_basic():
    ll = LinkedList()
    events = [
        make_event(1, "2025-12-01", "10:00"),
        make_event(2, "2025-10-01", "09:00"),
        make_event(3, "2025-11-01", "08:00"),
    ]
    for e in events:
        ll.insert(e)
    insertion_sort_linked_list(ll)
    assert list_to_keys(ll) == sorted(list_to_keys(ll))

def test_merge_sort_linked_list_stability():
    ll = LinkedList()
    items = [
        {"id":1,"title":"A","date":"2025-10-10","time":"10:00","location":"X"},
        {"id":2,"title":"B","date":"2025-10-10","time":"10:00","location":"Y"},
        {"id":3,"title":"C","date":"2025-10-09","time":"09:00","location":"Z"},
    ]
    for it in items:
        ll.insert(it)
    merge_sort_linked_list(ll)
    assert [e["id"] for e in ll.list_all()] == [3,1,2]

def test_quick_sort_linked_list_random():
    ll = LinkedList()
    import random
    days = [f"2025-10-{d:02d}" for d in range(1,6)]
    for i in range(50):
        d = random.choice(days)
        t = f"{random.randint(0,23):02d}:{random.randint(0,59):02d}"
        ll.insert({"id":i,"title":f"E{i}","date":d,"time":t,"location":"L"})
    quick_sort_linked_list(ll)
    keys = list_to_keys(ll)
    assert keys == sorted(keys)
