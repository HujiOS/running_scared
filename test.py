import random
import time
import os
for i in range(5):
  print("test-%s"%i)
  with open("output/file-%s.txt"%random.randint(0,100), "w+") as f:
    f.write("hello123%s"%random.randint(0,1000))
    f.write("hello123%s"%random.randint(0,1000))
    f.write("hello123%s"%random.randint(0,1000))
    f.write("hello123%s"%random.randint(0,1000))
    f.write("hello123%s"%random.randint(0,1000))
  time.sleep(5)
