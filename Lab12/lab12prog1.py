my_list = [50, 20, 70, 40, 90]

try:
    index = int(input("Enter an index: "))
    print(f"Value at index {index}: {my_list[index]}")
except IndexError:
    print("Error: The index is out of range.")
except ValueError:
    print("Error: Please enter a valid integer.")
