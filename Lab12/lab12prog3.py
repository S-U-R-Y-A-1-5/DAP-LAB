my_dict = {
    "apple": "A sweet red or green fruit",
    "banana": "A long yellow fruit",
    "orange": "A citrus fruit"
}

key = input("Enter a key to look up in the dictionary: ")

try:
    print(f"Definition: {my_dict[key]}")
except KeyError:
    print("Error: That key does not exist in the dictionary.")
