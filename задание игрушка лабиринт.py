import random

hp = 100
inv = []
max_inv = 5
x = 0
y = 0

maze = []
for i in range(4):
    maze.append([])
    for j in range(4):
        maze[i].append(random.choice(["пусто", "монстр", "монстр", "сундук"]))
maze[0][0] = "пусто"

ex = random.randint(0, 3)
ey = random.randint(0, 3)
while ex == 0 and ey == 0:
    ex = random.randint(0, 3)
    ey = random.randint(0, 3)
maze[ey][ex] = "выход"

inv.append("зелье")


def show_inv():
    if len(inv) == 0:
        print("Инвентарь пустой")
    else:
        print("Инвентарь", len(inv), "/", max_inv, ":", inv)


def heal():
    global hp
    if "зелье" in inv:
        inv.remove("зелье")
        hp = hp + 30
        if hp > 100:
            hp = 100
        print("Выпил зелье, HP:", hp)
        return True
    else:
        print("Нет зелья")
        return False


def chest():
    print("Нашел сундук!")
    things = ["зелье", "меч", "щит"]
    item = random.choice(things)
    print("Внутри:", item)
    if len(inv) >= max_inv:
        print("Инвентарь полный, предмет остался в сундуке")
    else:
        inv.append(item)
        print("Предмет в инвентаре")


def fight():
    global hp
    mhp = random.randint(25, 45)
    print("Ты наткнулся на монстра! HP монстра:", mhp)
    while mhp > 0 and hp > 0:
        print("Твое HP:", hp, "| HP монстра:", mhp)
        c = input("1 - ударить, 2 - зелье, 3 - бежать: ")
        if c == "1":
            dmg = random.randint(8, 18)
            if "меч" in inv:
                dmg = dmg + 5
            mhp = mhp - dmg
            print("Ты ударил на", dmg)
        elif c == "2":
            if heal() == False:
                continue
        elif c == "3":
            if random.randint(1, 2) == 1:
                print("Убежал!")
                return "fled"
            else:
                print("Не получилось убежать")
        else:
            print("Не понял")
            continue
        if mhp > 0:
            dmg = random.randint(5, 15)
            if "щит" in inv:
                dmg = dmg - 4
                if dmg < 1:
                    dmg = 1
            hp = hp - dmg
            print("Монстр ударил на", dmg)
    if hp <= 0:
        return "dead"
    print("Монстр убит")
    return "won"


print("ЛАБИРИНТ")
print("w a s d - ходить, i - инвентарь, p - зелье, q - выход")

while True:
    print("")
    print("Ты в клетке", x, y, "HP:", hp)
    cmd = input("Ход: ")
    nx = x
    ny = y
    if cmd == "w":
        ny = y - 1
    elif cmd == "s":
        ny = y + 1
    elif cmd == "a":
        nx = x - 1
    elif cmd == "d":
        nx = x + 1
    elif cmd == "i":
        show_inv()
        continue
    elif cmd == "p":
        heal()
        continue
    elif cmd == "q":
        print("Ты сдался")
        break
    else:
        print("Нет")
        continue

    if nx < 0 or nx > 3 or ny < 0 or ny > 3:
        print("Там стена")
        continue

    x = nx
    y = ny

    if maze[y][x] == "выход":
        print("Ты нашел выход! Победа!")
        break
    elif maze[y][x] == "монстр":
        res = fight()
        if res == "dead":
            print("Ты умер")
            break
        if res == "won":
            maze[y][x] = "пусто"
    elif maze[y][x] == "сундук":
        chest()
        maze[y][x] = "пусто"
    else:
        print("Тут пусто")
