
scores={'张三':100,'李四':20}
print(scores)
print(scores['张三'])
print( scores.get('张三1',10))
student = dict(name='jack',age=20)
del student['age']
student['李四']=98
print(student)
print(list(student))
print(student.values())
print(student.items())
for item in student:
    print(item,student.get(item))
d={}
print(d)

items = ['A','B','C']
values = [10,11,12]
d = {item.upper():value for item ,value in zip(items,values) }
print(d)