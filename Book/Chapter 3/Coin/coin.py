# Симулятор подбрасывания монеты 100 раз.

import random

attempt = 0
side = None
eagle = 0
tails = 0

while attempt < 100:
    side = random.randint(1,2)
    if side == 1:
        print('Орел')
        eagle += 1
    else:
        print('Решка')
        tails += 1
    attempt += 1
print('Орел выпал ', eagle, ' раз(а) ', 'Решка выпала ', tails, ' раз(а)')
