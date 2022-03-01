a = 3.14159
print(a,type(a))

n1 = 1.1
n2 = 2.2
print(n1+n2)

# 解决浮点数位数问题
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))