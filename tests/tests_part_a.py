# tests/test_part_a.py
from src.event import Event
from src.dynamic_array import DynamicArray
from src.singly_linked_list import SinglyLinkedList

def make_event(i):
    return Event(i, f"Title{i}", f"2025-11-{i:02d}", f"{10+i%12:02d}:00", f"Loc{i}")

def test_dynamic_array_basic():
    arr = DynamicArray()
    e1 = make_event(1); e2 = make_event(2); e3 = make_event(3)
    arr.insert(e1); arr.insert(e2); arr.insert(e3)
    assert len(arr) == 3
    assert arr.search_by_id(2) == e2
    assert arr.delete(2) is True
    assert arr.search_by_id(2) is None
    all_e = arr.list_all()
    assert [e.id for e in all_e] == [1,3]

def test_linked_list_basic():
    ll = SinglyLinkedList()
    e1 = make_event(1); e2 = make_event(2); e3 = make_event(3)
    ll.insert(e1); ll.insert(e2); ll.insert(e3)
    assert ll.size == 3
    assert ll.search_by_id(2) == e2
    assert ll.delete(2) is True
    assert ll.search_by_id(2) is None
    assert [e.id for e in ll.list_all()] == [1,3]
