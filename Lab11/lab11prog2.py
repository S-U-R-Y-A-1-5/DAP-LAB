names = ["Alice", "Arnold", "Bob", "Barry", "Charlie", "Cathy"]
grouped_names = {}
for i in names:
    first_letter = i[0].upper()
    if first_letter not in grouped_names:
            grouped_names[first_letter] = []
    grouped_names[first_letter].append(i)
print("Grouped Names:")
for key,value in grouped_names.items():
    print(f"{key}: {value}")

