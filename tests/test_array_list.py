# tests/test_array_list.py

from src.array_list import ArrayList

def test_array_insert_and_list():
    arr = ArrayList()

    events = [
        {"id": 1, "title": "Hackathon", "date": "2025-10-20", "time": "10:00", "location": "Hall A"},
        {"id": 2, "title": "Exam", "date": "2025-10-22", "time": "09:00", "location": "Room 101"},
        {"id": 3, "title": "Concert", "date": "2025-10-25", "time": "19:00", "location": "Auditorium"},
    ]

    for e in events:
        arr.insert(e)

    all_events = arr.list_all()
    print("\n[Array List] After Insert:", all_events)

    assert len(all_events) == 3
    assert all_events[0]["title"] == "Hackathon"

def test_array_search_and_delete():

    arr = ArrayList()
    e1 = {"id": 10, "title": "Talk", "date": "2025-11-01", "time": "15:00", "location": "Auditorium"}
    e2 = {"id": 11, "title": "Seminar", "date": "2025-11-02", "time": "12:00", "location": "Hall B"}
    arr.insert(e1)
    arr.insert(e2)

    found = arr.search_by_id(11)
    print("[Array List] Search Result for ID=11:", found)
    assert found["title"] == "Seminar"

    deleted = arr.delete(10)
    print("[Array List] After Deletion:", arr.list_all())
    assert deleted is True
    assert arr.search_by_id(10) is None
    

def test_array_delete_nonexistent():
    arr = ArrayList()
    e = {"id": 100, "title": "Workshop", "date": "2025-11-05", "time": "14:00", "location": "Lab 2"}
    arr.insert(e)
    deleted = arr.delete(999)
    print("[Array List] Attempt Delete ID=999:", deleted)
    assert deleted is False