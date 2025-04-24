contacts = {
    "Ashish": "9695145265",
    "Prince": "9875145635"
}
name = input("Enter contact name: ")
phone = input("Enter phone number: ")

if name in contacts:
    print(f"Updating number for {name}.")
else:
    print(f"Adding new contact for {name}.")
contacts[name] = phone
print("Updated Contacts:")
for i,j in contacts.items():
    print(f"{i}: {j}")
