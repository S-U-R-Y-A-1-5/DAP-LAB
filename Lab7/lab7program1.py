customer_name="Surya"
products_list=[("pen",50),("pencil",10),("books",15)]
print("Customer Invoice")
print("Name:",customer_name)
for products,price in products_list:
    print(f"{products}:{price}")
    
