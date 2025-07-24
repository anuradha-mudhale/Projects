import phonenumbers
from phonenumbers import geocoder

def get_location(phone_number):
    return geocoder.description_for_number(phone_number, "en")

phone_numbers = [
    "+917294536271", "+918878586271", "+12136574429", "+201234567890",
    "+917822809421", "+201234567898", "+919421114125", "+12136594429",
    "+12136579029", "+917890809422", "+917057870252", "+917822809424",
    "+201234567890", "+917822809422", "+917822809423", "+917822809424",
    "+12136574429"
]

print("Choose an option:")
print("1. Enter a phone number manually")
print("2. Display locations for numbers in the list")

option = input("Enter your choice (1 or 2): ").strip()

if option == "1":
    phone_number = input("Enter the phone number: ").strip()
    parsed_number = phonenumbers.parse(phone_number)
    location = get_location(parsed_number)
    print(f"Location for {phone_number}: {location}")
elif option == "2":
    print("\nPhone Numbers Location:")
    for number in phone_numbers:
        parsed_number = phonenumbers.parse(number)
        location = get_location(parsed_number)
        print(f"{number}: {location}")
else:
    print("Invalid option selected.")
