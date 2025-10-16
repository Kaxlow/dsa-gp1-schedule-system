from datetime import datetime

# Define functions to convert campus event's date and time strings to date-time objects for comparison
def get_event_dt_start(event):
  return datetime.strptime(f"{event["date"]} {event["time_start"]}", "%Y-%m-%d %H:%M")

def get_event_dt_end(event):
  return datetime.strptime(f"{event["date"]} {event["time_end"]}", "%Y-%m-%d %H:%M")