import random # 0-1的随机数
import math
import time
start=time.time()
print(math.floor(random.random()*10+1))
print(math.ceil(random.random()*10+1))
t= time.localtime()
print(t.tm_hour)
print(t.tm_mon)
end=time.time()

print(f"need time:{end-start}")

