# Version 3: String and Date Formatting
from datetime import datetime
print("STUDENT EVENT REGISTRATION")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
section = input("Enter your section: ")
event_name = input("Enter the event name: ")
event_year = input("Enter event year: ")
event_month = input("Enter event month: ")
event_day = input("Enter event day: ")

# String formatting
first_name = first_name.strip().title()
last_name = last_name.strip().title()
section = section.strip().upper()
event_name = event_name.strip().title()

full_name = first_name + " " + last_name
name_code = full_name.upper()

# Date formatting
event_date = datetime(
    int(event_year),
    int(event_month),
    int(event_day)
)
formatted_date = event_date.strftime("%B") + " " + str(event_date.day) + ", " + str(event_date.year)

print("\nStudent Event Registration Summary")
print("Name:", full_name)
print("Name Code:", name_code)
print("Section:", section)
print("Event:", event_name)
print("Event Date:", formatted_date)

print("Language Used: Python")
print("String Feature Used: strip(), title(), upper()")
print("Date/Time Feature Used: datetime")
print("\nRegistration record created successfully.")
