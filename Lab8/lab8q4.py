org_list=[1,1,2,3,4,4,5,1]
first_list=[]
second_list=[]
n=3
pos=0
for i in org_list:
    if pos<n:
        first_list.append(i)
    else:
        second_list.append(i)
    pos+=1
print("first list:",first_list)
print("second list:",second_list)
    
