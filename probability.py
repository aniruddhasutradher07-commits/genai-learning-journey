import random

# 1000 baar dice roll karke dekhte hain kitni baar "3" aata hai
count_2 = 0
coin_toss = 1000

for i in range(coin_toss):
    roll = random.randint(1, 2)
    if roll == 1:
        count_2 = count_2 + 1

probability = count_2 / coin_toss
print("Heads aane ki probability:", probability)
