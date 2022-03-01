a = 10
lst= ['hello','world',98]
print(id(lst))
print(type(lst))
print(lst)
# 创建列表第二种方式，使用内置函数list
lst2 = list(['hello','world',98])
print(lst2.index('hello'))
# print(lst2.index('hello',1,2))
print(lst2[2])

lit = [1,2,3,4,5,6,7,8,9]
print(lit[1:6:1])

lst.append(100)
lst.insert(1,90)
print('添加到元素之后',lst,id(lst))
lst.remove(90)
print('添加到元素之后',lst,id(lst))
# 根据索引移除，如果不指定参数，那么删除列表最后一个参数
lst.pop(1)
print('添加到元素之后',lst,id(lst))
lst.clear()
print('添加到元素之后',lst,id(lst))
del lst  #删除列表
print('添加到元素之后',lst,id(lst))

