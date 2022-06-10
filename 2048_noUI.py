import random

# 矩阵大小（游戏难度）
SIZE = 4

# map存储矩阵中的数字
map = [[0 for i in range(SIZE)] for i in range(SIZE)]

# 游戏分数
score = 0


# 展示矩阵
def show(M):
    print("\n" + "使用W A S D控制方向", end="")
    print("\n" + " " * 25 + "Score: " + "{:}".format(score), end="")
    for i in range(SIZE):
        print("\n")
        for j in range(SIZE):
            print("{: >6}".format(M[i][j]), end="")
    print("\n")


# 随机生成新数字
def add(M):
    numOfZero = 0
    cnt = 0
    for r in range(SIZE):
        for c in range(SIZE):
            if M[r][c] == 0:
                numOfZero += 1
    if numOfZero >= 2:
        numOfZero = 2
    while True:
        p = random.randint(0, SIZE * SIZE - 1)
        if M[p // SIZE][p % SIZE] == 0:
            x = random.choice([2, 2, 2, 4])
            M[p // SIZE][p % SIZE] = x
            cnt += 1
        if cnt == numOfZero:
            break
    return M


# 判断游戏结束
def over(M):
    for r in range(SIZE):
        for c in range(SIZE):
            if M[r][c] == 0:
                return False
    for r in range(SIZE):
        for c in range(SIZE - 1):
            if M[r][c] == M[r][c + 1]:
                return False
    for r in range(SIZE - 1):
        for c in range(SIZE):
            if M[r][c] == M[r + 1][c]:
                return False
    return True


# 计算玩家每次操作后矩阵的更新。这个函数只适用于向左移动，其他方向不适用。
def caculate(M):
    global score
    changed = False
    for a in M:
        b = []
        last = 0
        for v in a:
            if v != 0:
                if v == last:
                    s = b.pop() * 2
                    b.append(s)
                    score += s
                    last = 0
                else:
                    b.append(v)
                    last = v
        b += [0] * (SIZE - len(b))  # 弥补本行剩下的元素
        for i in range(SIZE):
            if a[i] != b[i]:
                changed = True
        a[:] = b
    return M, changed


# 将整个矩阵逆时针旋转90度
def rotate90(M):
    M = [[M[c][r] for c in range(SIZE)] for r in reversed(range(SIZE))]
    return M


# 玩家选择向上时
def moveUp():
    global map
    map = rotate90(map)  # 先逆时针旋转90度，原本向上的操作变成了向左操作，这时就可以调用caculate函数。
    if caculate(map)[1]:
        map = add(map)
    map = rotate90(map)
    map = rotate90(map)
    map = rotate90(map)  # 操作完成后再旋转3个90度，总共旋转360度，矩阵方向不变。


def moveRight():
    global map
    map = rotate90(map)
    map = rotate90(map)
    if caculate(map)[1]:
        map = add(map)
    map = rotate90(map)
    map = rotate90(map)


def moveDown():
    global map
    map = rotate90(map)
    map = rotate90(map)
    map = rotate90(map)
    if caculate(map)[1]:
        map = add(map)
    map = rotate90(map)


def moveLeft():
    global map
    if caculate(map)[1]:
        map = add(map)


map = add(map)
show(map)
while not over(map):
    cmd = input()
    if cmd == "w":
        moveUp()
    if cmd == 's':
        moveDown()
    if cmd == 'a':
        moveLeft()
    if cmd == 'd':
        moveRight()
    show(map)
print("Game Over!\nYour score is: ", end='')
print(score)
