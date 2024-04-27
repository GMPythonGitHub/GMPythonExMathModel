import random
xx = list(range(-49,50))

for _ in range(3):
    print(random.choice(xx), random.choice(xx))



print(random.choices(xx, k=10))