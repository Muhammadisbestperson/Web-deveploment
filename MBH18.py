student_data ={   'id1':
               {'name':['Muhammad'],
                'class':["VI"],
                'subject integrations':['Geography,History,Science']},
                 'id2':
                {'name':['Ibrahim'],
                 'class':['III'],
                 'Subject integrations':['Urdu,Maths,English']},
                 'id3':
                 {'name':['Abbas'],
                  'class':['X'],
                  'Subject integrations':['Maths type 3,Biology,Chemistry']},
                  'id4':
                 {'name':['Khalil'],
                  'class':['VIII'],
                  'Subject integrations':['Maths ,Computer,Chemistry']},       
}
result={}
for key,value in student_data.items():
    if value not in result.values():
        result[key]=value
print(result)       