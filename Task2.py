original_list=[]
for i in range(1,11):
    original_list.append(i)
print(original_list)    
r1=original_list[0:5]
print(f'Extracted first five elements: {r1}')
r2=r1[::-1]
print(f'Reversed extracted elements :{r2}')    
