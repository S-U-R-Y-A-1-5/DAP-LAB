name=input("Enter Student name:")
per=float(input("Enter the percentage of the student:"))
if per>=90:
    res="A"
elif per>=80 and per<=90:
    res="B"
elif per>=70 and per<=80:
    res="C"
elif per>=60 and per<=50:
    res="D"
else:
    res="E"
print(f"Student name:{name}\nFinal Grade:{res}")
