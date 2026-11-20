# Version 2: Added String Formatting
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

event_date = event_month + "/" + event_day + "/" + event_year

print("\nStudent Event Registration Summary")
print("Name:", full_name)
print("Name Code:", name_code)
print("Section:", section)
print("Event:", event_name)
print("Event Date:", event_date)

print("Language Used: Python")
print("String Feature Used: strip(), title(), upper()")
print("\nRegistration record created successfully.")
