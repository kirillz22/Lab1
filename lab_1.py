import os
import time


RED = '\u001b[41m'
WHITE = '\u001b[47m'
BLACK = '\u001b[40m'
GREEN = '\u001b[42m'
END = '\u001b[0m'


# 1. Флаг Швейцарии (15 строк, ширина 30 пробелов)
def flag():
   for i in range(15):
       if 6 <= i <= 8:
           print(RED + ' ' * 4 + WHITE + ' ' * 22 + RED + ' ' * 4 + END)
       elif 2 <= i <= 12:
           print(RED + ' ' * 12 + WHITE + ' ' * 6 + RED + ' ' * 12 + END)
       else:
           print(RED + ' ' * 30 + END)


# 2. Узор j (два кольца), чёрные кольца на белом фоне
ring = ['..###..',
        '.#####.',
        '##...##',
        '##...##',
        '##...##',
        '.#####.',
        '..###..']
pattern = []
for k in range(2):                                # узор повторяется по вертикали
    for row in ring:
        pattern.append((row + row + '.') * 4)     # два кольца + промежуток, повтор по горизонтали
    pattern.append('.' * 60)                      # пустая строка между рядами


def pattern_j():
    print()
    for row in pattern:
        print(row[:30].replace('#', BLACK + '  ' + END).replace('.', WHITE + '  ' + END))


# 3. Анимация из 3 кадров
def animation():
    for i in range(3, 0, -1):  # 3, 2, 1
        os.system('cls' if os.name == 'nt' else 'clear')
        print(RED + '  ' + str(i) + '  ' + END)
        time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(GREEN + ' Go! ' + END)


def sequence():
    file = open('sequence.txt', 'r')
    inside = []     # числа от -3 до 3
    outside = []    # остальные числа
    for line in file:
        if -3 <= float(line) <= 3:
            inside.append(float(line))
        else:
            outside.append(float(line))
    file.close()

    total = len(inside) + len(outside)
    print(GREEN + ' ' * int(len(inside) / 5) + END + ' от -3 до 3: ' + str(round(len(inside) / total * 100, 1)) + '%')
    print(RED + ' ' * int(len(outside) / 5) + END + ' остальные: ' + str(round(len(outside) / total * 100, 1)) + '%')


#flag()
#pattern_j()
#animation()
#sequence()
