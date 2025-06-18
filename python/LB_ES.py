def is_facing_west():
    turn(3)
    result = is_facing_north()
    turn_left()
    return result

def turn(times):  # 改参数名避免覆盖内置类型
    for i in range(times):
        turn_left()
        
def new_move(steps):  # 改参数名避免覆盖内置类型
    for i in range(steps):
        move()
        
def harvest_one_row():
    while object_here():
        take()
    else:
        move()

# move to the field
turn_left()
new_move(2)
turn(3)
new_move(2)

# 原有的3行收割逻辑
for i in range(3):
    while is_facing_west():
        for _ in range(6):
            harvest_one_row()
        for _ in range(2):
            turn(3)
            move() 
    else:
        for _ in range(6):
            harvest_one_row()
        for _ in range(2):
            turn(1)
            move()

# 新增：收割剩余5个胡萝卜的程序
def harvest_remaining_carrots():
 
    
    # 收割剩余的5个胡萝卜（具体路径需要根据实际布局调整）
    for _ in range(6):
        while object_here():
            take()
        move()  # 移动到下一个位置

# 执行剩余胡萝卜的收割
harvest_remaining_carrots()
new_move(1)