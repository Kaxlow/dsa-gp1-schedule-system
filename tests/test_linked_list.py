# tests/test_linked_list.py

from src.linked_list import LinkedList

def test_linked_insert_and_list():
    ll = LinkedList()
    events = [
        {"id": 1, "title": "Concert", "date": "2025-10-30", "time": "18:00", "location": "Stadium"},
        {"id": 2, "title": "Workshop", "date": "2025-11-05", "time": "14:00", "location": "Lab 2"},
        {"id": 3, "title": "Hackathon", "date": "2025-11-10", "time": "10:00", "location": "Main Hall"},
    ]

    for e in events:
        ll.insert(e)

    all_events = ll.list_all()
    print("\n[Linked List] After Insert:", all_events)
    assert len(all_events) == 3
    assert all_events[-1]["title"] == "Hackathon"

def test_linked_search_and_delete():
    ll = LinkedList()
    e1 = {"id": 5, "title": "Talk", "date": "2025-11-01", "time": "15:00", "location": "Auditorium"}
    e2 = {"id": 6, "title": "Exam", "date": "2025-11-03", "time": "09:00", "location": "Room 202"}
    ll.insert(e1)
    ll.insert(e2)

    found = ll.search_by_id(5)
    print("[Linked List] Search Result for ID=5:", found)
    assert found == e1

    ll.delete(5)
    print("[Linked List] After Deleting ID=5:", ll.list_all())
    assert ll.search_by_id(5) is None

def test_linked_delete_nonexistent():
    ll = LinkedList()
    e = {"id": 100, "title": "Seminar", "date": "2025-11-15", "time": "12:00", "location": "Hall C"}
    ll.insert(e)
    deleted = ll.delete(500)
    print("[Linked List] Attempt Delete ID=500:", deleted)
    assert deleted is False
