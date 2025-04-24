expected_items = {"A", "B", "C", "D", "E"}
available_items = {"A", "C", "E"}
missing_items=set()
for i in expected_items:
    if i not in available_items:
        missing_items.add(i)
print("Items That are missing in the warehouse are:",missing_items)
        
        
