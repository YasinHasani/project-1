x1 = int(input("عدد خود را وارد کنيد ="))
x2 = int(input("عدد خود را وارد کنيد ="))
y1 = int(input("عدد خود را وارد کنيد ="))
y2 = int(input("عدد خود را وارد کنيد ="))

import math

f = (x2-x1)**2
d = (y2-y1)**2
c = math.sqrt(f+d)
print(c)
