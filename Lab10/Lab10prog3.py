all_customers = {"John", "Mary", "Steve", "Ana"}
returned_customers = {"Mary", "Ana"}
never_returned=all_customers.difference(returned_customers)
print("Customers who bought a product but never returned are:",never_returned)
