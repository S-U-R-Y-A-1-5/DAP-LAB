my_list=[10,25,16,98]
largest=my_list[0]
smallest=my_list[0]
for i in my_list:
    if i>largest:
        largest=i
    if i<smallest:
        smallest=i

print(f"Largest number is:{largest}")
print(f"Smallest number is:{smallest}")
