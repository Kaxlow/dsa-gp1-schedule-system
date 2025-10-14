class Event:
    def __init__(self, event_id, title, date, time, location):
        self.id = event_id
        self.title = title
        self.date = date  # "YYYY-MM-DD"
        self.time = time  # "HH:MM"
        self.location = location

