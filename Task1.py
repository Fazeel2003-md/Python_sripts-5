try:
    name=input('Enter the Students name : ')
    marks={
        'fazeel':90,
        'Alice':85,
        'Nazeer':92,
        'Rehan':88
    }
except KeyError:
    print("student not found")
else:
    r=marks[name]
    print(f'{name} marks:{r}')    
        
