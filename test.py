import time

test = time.time()

for i in range(1000000):
    random = i

test2 = time.time()

print(test - test2)