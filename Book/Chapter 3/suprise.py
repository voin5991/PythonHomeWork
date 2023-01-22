# Симулятор пирожка с "Сюрпризом"

import random

print(input("Нажмите Enter чтобы получить один из пяти возможных призов: "))
prize = random.randint(1,5)

if prize == 1:
    print("""
     ___________________________$$
     _________________________$$$$
     _______________________$$$$$$
     ______________________$$$$$$
     ______________________$$$$
     ______________________$$
     _________$$$$$$$$$$$$$_$$$$$$$$$$$$$
     ______$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
     ____$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
     ___$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
     __$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
     _$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
     _$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
     _$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
     _$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
     __$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
     ___$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
     ____$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
     _____$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
     ______$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
     ________$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
     __________$$$$$$$$$$$$$$$$$$$$$$$$$
     ____________$$$$$$$$$$$$$$$$$$$$$
     ______________$$$$$$$$__$$$$$$$

    """)
    print("Поздравляю! Вы выиграли IPhone!")
elif prize == 2:
    print("""
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$_$$$$$$$$$$$$$$$$_$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$__$$$$$$$$$$$$$$_$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$_______________$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$___________________$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$____$$$_________$$$____$$$$$$$$$$$$$
    $$$$$$$$$$$$$_____$$$_________$$$_____$$$$$$$$$$$$
    $$$$$$$$$$$$___________________________$$$$$$$$$$$
    $$$$$$$$$$$$___________________________$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    $$$$$____$$$____________________________$$$____$$$
    $$$$______$$____________________________$$______$$
    $$$$______$$____________________________$$______$$
    $$$$______$$____________________________$$______$$
    $$$$______$$____________________________$$______$$
    $$$$______$$____________________________$$______$$
    $$$$______$$____________________________$$______$$
    $$$$______$$____________________________$$______$$
    $$$$______$$____________________________$$______$$
    $$$$$____$$$____________________________$$$____$$$
    $$$$$$$$$$$$____________________________$$$$$$$$$$
    $$$$$$$$$$$$____________________________$$$$$$$$$$
    $$$$$$$$$$$$___________________________$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$______$$$$$$_____$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    """)
    print("Поздравляю! Вы выиграли Смартфон!")
elif prize == 3:
    print("""
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1111111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11111111111111111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶111111111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶111111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶1111111111¶¶¶¶¶¶¶¶ 
    ¶¶¶¶¶¶¶11111111111111¶¶¶¶¶¶¶¶¶1111111111111¶¶¶¶¶¶¶ 
    ¶¶¶¶¶¶111111111111111111¶¶¶11111111111111111¶¶¶¶¶¶ 
    ¶¶¶¶¶11111111111111111111¶1111111111111111111¶¶¶¶¶ 
    ¶¶¶¶¶111111111111¶¶¶1111111111¶¶¶1111111111111¶¶¶¶ 
    ¶¶¶¶111111111111¶¶¶¶¶11111111¶¶¶¶¶1111111111111¶¶¶ 
    ¶¶¶¶11111111111¶¶¶¶¶¶11111111¶¶¶¶¶¶111111111111¶¶¶ 
    ¶¶¶11111111111¶¶¶¶¶111111111111¶¶¶¶¶11111111111¶¶¶ 
    ¶¶¶1111111111¶¶¶¶¶11111111111111¶¶¶¶¶1111111111¶¶¶ 
    ¶¶¶111111111¶¶¶¶11111111111111111¶¶¶¶¶111111111¶¶¶ 
    ¶¶¶11111111¶¶¶¶1111111111111111111¶¶¶¶¶11111111¶¶¶ 
    ¶¶¶¶111111¶¶¶¶¶11111111111111111111¶¶¶¶¶1111111¶¶¶ 
    ¶¶¶¶11111¶¶¶¶111111111111111111111111¶¶¶¶11111¶¶¶¶ 
    ¶¶¶¶¶1111¶¶¶1111111111111111111111111¶¶¶¶¶111¶¶¶¶¶ 
    ¶¶¶¶¶111¶¶¶1111111111111111111111111111¶¶¶111¶¶¶¶¶ 
    ¶¶¶¶¶¶11¶¶¶1111111111111111111111111111¶¶¶11¶¶¶¶¶¶ 
    ¶¶¶¶¶¶¶¶¶¶111111111111111111111111111111¶¶¶¶¶¶¶¶¶¶ 
    ¶¶¶¶¶¶¶¶¶¶111111111111111111111111111111¶¶¶¶¶¶¶¶¶¶ 
    ¶¶¶¶¶¶¶¶¶¶¶1111111111111111111111111111¶¶¶¶¶¶¶¶¶¶¶ 
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶11111111111111111111111¶¶¶¶¶¶¶¶¶¶¶¶¶ 
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1111111111111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶11¶¶¶¶¶¶¶11¶¶111111111¶¶¶¶¶11111111¶¶¶11¶¶¶¶¶¶11¶
    ¶¶111¶¶¶¶11¶¶¶11¶¶¶¶¶¶11¶¶¶111¶¶¶¶¶111¶¶11¶¶¶¶11¶¶
    ¶¶¶¶11¶111¶¶¶¶11¶¶¶¶¶¶11¶¶11¶¶¶¶¶¶¶¶¶11¶¶11¶¶11¶¶¶
    ¶¶¶¶¶111¶¶¶111111111111¶¶¶11¶¶¶¶¶¶¶¶¶11¶¶¶1111¶¶¶¶
    ¶¶¶¶¶111¶¶¶1111111111111¶¶11¶¶¶¶¶¶¶¶¶11¶¶¶1111¶¶¶¶
    ¶¶¶111¶111¶¶¶¶11¶¶¶¶¶¶¶11¶11¶¶¶¶¶¶¶¶¶11¶¶11¶¶11¶¶¶
    ¶¶111¶¶¶¶11¶¶¶11¶¶¶¶¶¶¶11¶111¶¶¶¶¶¶¶111¶11¶¶¶¶11¶¶
    ¶11¶¶¶¶¶¶¶11¶¶1111111111¶¶¶¶111111111¶¶11¶¶¶¶¶¶11¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶11111111¶¶¶¶¶¶¶11¶¶¶¶¶¶¶¶¶¶11¶¶1111111111111¶
    ¶¶¶11111¶¶¶1111¶¶¶¶¶111¶¶¶¶¶¶¶¶¶11¶¶1111111111111¶
    ¶¶111¶¶¶¶¶¶¶¶¶111¶¶¶1111¶¶¶¶¶¶¶¶11¶¶111¶¶¶¶¶¶¶¶¶¶¶
    ¶111¶¶¶¶¶¶¶¶¶¶¶11¶¶¶11¶111¶¶¶¶¶¶11¶¶111¶¶¶¶¶¶¶¶¶¶¶
    ¶11¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶11¶¶111¶¶¶¶¶11¶¶111¶¶¶¶¶¶¶¶¶¶¶
    ¶11¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶11¶¶¶111¶¶¶¶11¶¶111111111111¶¶
    ¶11¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶11¶¶¶¶¶11¶¶¶11¶¶111¶¶¶¶¶¶¶¶¶¶¶
    ¶111¶¶¶¶¶¶¶¶¶¶¶111¶¶11¶¶¶¶¶¶111¶11¶¶111¶¶¶¶¶¶¶¶¶¶¶
    ¶¶111¶¶¶¶¶¶¶¶¶111¶¶¶11¶¶¶¶¶¶¶11111¶¶111¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶1111¶¶¶¶¶1111¶¶¶¶11¶¶¶¶¶¶¶¶1111¶¶111¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶111111111¶¶¶¶¶¶11¶¶¶¶¶¶¶¶¶¶11¶¶1111111111111¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    """)
    print('Поздравляю! Вы выиграли XboxOne!')
elif prize == 4:
    print('''
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶11111111111111¶¶¶¶¶¶¶¶¶111111111¶¶¶¶¶¶¶¶¶¶¶11¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶111¶¶¶¶¶¶¶111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1111¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶¶¶¶¶¶11¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11¶11¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶111¶¶¶¶¶¶¶11¶¶¶¶¶¶¶¶¶¶¶¶¶¶111¶¶11¶¶¶
    ¶¶¶¶1111111111111¶¶¶¶¶¶¶11¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶¶¶11¶¶¶
    ¶¶11111111111111¶¶¶¶¶¶¶¶11¶¶¶¶¶¶¶¶¶¶¶111¶¶¶¶¶11¶¶¶
    ¶¶111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶¶¶¶¶¶¶¶¶11¶¶¶¶¶¶¶11¶¶¶
    ¶¶11¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶¶¶¶¶¶¶111¶¶¶¶¶¶¶¶11¶¶¶
    ¶¶11¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶¶¶¶¶¶1111111111111111¶
    ¶¶11¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶111¶¶¶¶¶¶11111111111111111¶
    ¶¶11¶¶¶¶¶¶¶¶¶¶¶¶111111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11111111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11111111111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11111111¶¶1111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11111111¶¶¶1111111¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11111111¶¶¶11111111¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11111111¶¶¶11111111¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11111111¶¶¶11111111¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11111111¶¶¶11111111¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11111111¶¶¶11111111¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11111111¶¶¶11111111¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11111111¶¶¶1111111¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶11111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶111111¶¶11111111¶¶¶¶¶¶111111111¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶11111111111¶¶11111111¶1111111111111111111¶¶¶
    ¶¶111111111111¶¶¶¶¶11111111¶1111111¶¶¶¶¶¶¶1111111¶
    ¶11111111¶¶¶¶¶¶¶¶¶¶11111111¶11¶¶¶¶¶¶¶¶1111111111¶¶
    ¶¶1111111¶¶¶11111¶¶11111111¶¶¶¶¶¶1111111111111¶¶¶¶
    ¶¶¶¶¶¶11111111111¶¶11111111¶¶111111111111¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11111111¶11111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶111111¶1111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ''')
    print('Поздравляю! Вы выиграли PlayStation 4!')
elif prize == 5:
    print('''
    ────────────────────░███░
    ───────────────────░█░░░█░
    ──────────────────░█░░░░░█░
    ─────────────────░█░░░░░█░
    ──────────░░░───░█░░░░░░█░
    ─────────░███░──░█░░░░░█░
    ───────░██░░░██░█░░░░░█░
    ──────░█░░█░░░░██░░░░░█░
    ────░██░░█░░░░░░█░░░░█░
    ───░█░░░█░░░░░░░██░░░█░
    ──░█░░░░█░░░░░░░░█░░░█░
    ──░█░░░░░█░░░░░░░░█░░░█░
    ──░█░░█░░░█░░░░░░░░█░░█░
    ─░█░░░█░░░░██░░░░░░█░░█░
    ─░█░░░░█░░░░░██░░░█░░░█░
    ─░█░█░░░█░░░░░░███░░░░█░
    ░█░░░█░░░██░░░░░█░░░░░█░
    ░█░░░░█░░░░█████░░░░░█░
    ░█░░░░░█░░░░░░░█░░░░░█░
    ░█░█░░░░██░░░░█░░░░░█░
    ─░█░█░░░░░████░░░░██░
    ─░█░░█░░░░░░░█░░██░█░
    ──░█░░██░░░██░░█░░░█░
    ───░██░░███░░██░█░░█░
    ────░██░░░███░░░█░░░█░
    ──────░███░░░░░░█░░░█░
    ──────░█░░░░░░░░█░░░█░
    ──────░█░░░░░░░░░░░░█░
    ──────░█░░░░░░░░░░░░░█░
    ──────░█░░░░░░░░░░░░░█░
    ████──░█░████░░░░░░░░█░
    █──█──████──████░░░░░█░
    █──█──█──█──█──████████
    █──█──████──█──█──────█
    █──█──█──█────██──██──█
    █──████──█──█──█──────█
    █─────█──█──█──█──█████
    ███████──████──█──────█
    ──────████──██████████
    ''')
    print('Утешительный приз! Лайк Вам!!!')
else:
    print('Простите, но, кажется удача сегодня не на Вашей стороне.')
