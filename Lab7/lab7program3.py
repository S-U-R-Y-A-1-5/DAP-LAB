message=input("Enter the user message:")
print("Before removing extra space:",message)
res="".join(message.split())
print("after removing the extra space:",res)
