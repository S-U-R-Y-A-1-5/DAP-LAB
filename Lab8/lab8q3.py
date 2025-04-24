numbers=[1,2,1,3,4,3,5,6,2]
count=[0,0,0,0,0,0,0,0,0]
duplicates=[]
for i in numbers:
    count[i]+=1
    if count[i]>=2:
        duplicates.append(i)
print(f"Duplicate numbers are:{duplicates}")
