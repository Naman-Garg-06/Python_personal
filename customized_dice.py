import random,time

print("Rolling...")
temp = []
for i in range(5):
    temp.append(random.randint(1,6))
time.sleep(2)
print("Rolled")
print(max(temp))
