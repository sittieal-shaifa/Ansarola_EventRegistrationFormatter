# Version 1: Basic Input and Output

print("STUDENT EVENT REGISTRATION")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
section = input("Enter your section: ")
event_name = input("Enter the event name: ")
event_year = input("Enter event year: ")
event_month = input("Enter event month: ")
event_day = input("Enter event day: ")

full_name = first_name + " " + last_name
event_date = event_month + "/" + event_day + "/" + event_year

print("\nStudent Event Registration Summary")
print("Name:", full_name)
print("Section:", section)
print("Event:", event_name)
print("Event Date:", event_date)

print("\nRegistration record created successfully.")
