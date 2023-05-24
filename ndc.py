import pyxel

# initialization
pyxel.init(128, 128, title="Nuit Du Code", fps=30, quit_key=pyxel.KEY_P)

pyxel.load("theme3.pyxres")

xBulletPlayer1 = 0
yBulletPlayer1 = -10
faxb1 = 16
fayb1 = 72

xBulletPlayer2 = 0
yBulletPlayer2 = -10
faxb2 = 16
fayb2 = 72

def TIMER(time):
    for i in range(time):
        if(pyxel.frame_count % 30 == 0):
            time -= 1
    return("finish")
    print("finish")
    
def void(sprite):
    global xPlayer1, yPlayer1, xPlayer2, yPlayer2, factorPlayer1, factorPlayer2, global_speed, dirPlayer1, dirPlayer2, fax1, fax2, fay1, fay2, flip_axis1, flip_axis2, xBulletPlayer1, yBulletPLayer1, xBulletPlayer2, yBulletPlayer2
    if(sprite == "PLAYER_1"):
        xPlayer1 = -10
        yPlayer1 = -10
    elif(sprite == "PLAYER_2"):
        xPlayer2 = -10
        yPlayer = -10

TIMER(3)
# x position of first player
xPlayer1 = 60
# y position of first player
yPlayer1 = 10
# direction for first player
dirPlayer1 = "West"
# global factor of first player
factorPlayer1 = 1
# x position of second player
xPlayer2 = 60
# y position of second player
yPlayer2 = 10
# direction for second player
dirPlayer2 = "East"
# global factor of second player
factorPlayer2 = 1
# game speed
global_speed = 1

flip_axis1 = False
flip_axis2 = False

fax1 = 24
fay1 = 64
fax2 = 24
fay2 = 72
# top right corner
def ctr(PLAYER, x_or_y):
    if (PLAYER == "PLAYER_1"):
        if (x_or_y == "x"):
            return xBulletPlayer1 + 9
        if (x_or_y == "y"):
            return yBulletPlayer1
    if (PLAYER == "PLAYER_2"):
        if (x_or_y == "x"):
            return xBulletPlayer2 + 9
        if (x_or_y == "y"):
            return yBulletPlayer2
# top left corner
def ctl(PLAYER, x_or_y):
    if (PLAYER == "PLAYER_1"):
        if (x_or_y == "x"):
            return xBulletPlayer1
        if (x_or_y == "y"):
            return yBulletPlayer1
    if (PLAYER == "PLAYER_2"):
        if (x_or_y == "x"):
            return xBulletPlayer2
        if (x_or_y == "y"):
            return yBulletPlayer2
# bottom right corner
def cbr(PLAYER, x_or_y):
    if (PLAYER == "PLAYER_1"):
        if (x_or_y == "x"):
            return xBulletPlayer1 + 9
        if (x_or_y == "y"):
            return yBulletPlayer1 + 9
    if (PLAYER == "PLAYER_2"):
        if (x_or_y == "x"):
            return xBulletPlayer2 + 9
        if (x_or_y == "y"):
            return yBulletPlayer2 + 9
# bottom left corner
def cbl(PLAYER, x_or_y):
    if (PLAYER == "PLAYER_1"):
        if (x_or_y == "x"):
            return xPlayer1
        if (x_or_y == "y"):
            return yPlayer1 + 9
    if (PLAYER == "PLAYER_2"):
        if (x_or_y == "x"):
            return xPlayer2
        if (x_or_y == "y"):
            return yPlayer2 + 9

def ctr2(PLAYER, x_or_y):
    if (PLAYER == "PLAYER_1"):
        if (x_or_y == "x"):
            return xPlayer1 + 9
        if (x_or_y == "y"):
            return yPlayer1
    if (PLAYER == "PLAYER_2"):
        if (x_or_y == "x"):
            return xPlayer2 + 9
        if (x_or_y == "y"):
            return yPlayer2
# top left corner
def ctl2(PLAYER, x_or_y):
    if (PLAYER == "PLAYER_1"):
        if (x_or_y == "x"):
            return xPlayer1
        if (x_or_y == "y"):
            return yPlayer1
    if (PLAYER == "PLAYER_2"):
        if (x_or_y == "x"):
            return xPlayer2
        if (x_or_y == "y"):
            return yPlayer2
# bottom right corner
def cbr2(PLAYER, x_or_y):
    if (PLAYER == "PLAYER_1"):
        if (x_or_y == "x"):
            return xPlayer1 + 9
        if (x_or_y == "y"):
            return yPlayer1 + 9
    if (PLAYER == "PLAYER_2"):
        if (x_or_y == "x"):
            return xPlayer2 + 9
        if (x_or_y == "y"):
            return yPlayer2 + 9
# bottom left corner
def cbl2(PLAYER, x_or_y):
    if (PLAYER == "PLAYER_1"):
        if (x_or_y == "x"):
            return xPlayer1
        if (x_or_y == "y"):
            return yPlayer1 + 9
    if (PLAYER == "PLAYER_2"):
        if (x_or_y == "x"):
            return xPlayer2
        if (x_or_y == "y"):
            return yPlayer2 + 9
            
def gravity1(direction):
    global xPlayer1, yPlayer1, xPlayer2, yPlayer2, factorPlayer1, factorPlayer2, global_speed, dirPlayer1, dirPlayer2, fax1, fax2, fay1, fay2, flip_axis1, flip_axis2, xBulletPlayer1, yBulletPLayer1, xBulletPlayer2, yBulletPlayer2
    if (direction == "West"):
        for i in range(128):
            xBulletPlayer1 -= 1
    elif (direction == "East"):
        for i in range(128):
            xBulletPlayer1 += 1
            
def gravity2(direction):
    xPlayer1, yPlayer1, xPlayer2, yPlayer2, factorPlayer1, factorPlayer2, global_speed, dirPlayer1, dirPlayer2, fax1, fax2, fay1, fay2, flip_axis1, flip_axis2, xBulletPlayer1, yBulletPLayer1, xBulletPlayer2, yBulletPlayer2
    if (direction == "West"):
        for i in range(128):
            xBulletPlayer2 -= 1
    elif (direction == "East"):
        for i in range(128):
            xBulletPlayer2 += 1

# function update()
def update():
    
    # import global variables
    global xPlayer1, yPlayer1, xPlayer2, yPlayer2, factorPlayer1, factorPlayer2, global_speed, dirPlayer1, dirPlayer2, fax1, fax2, fay1, fay2, flip_axis1, flip_axis2, xBulletPlayer1, yBulletPLayer1, xBulletPlayer2, yBulletPlayer2
    
    """display variables for debug"""
    
    if (dirPlayer1 == "West"):
        flip_axis1 = True
        fax1 = 32
        fay1 = 64
    if (dirPlayer1 == "East"):
        flip_axis1 = False
        fax1 = 24
        fay1 = 64
    if (dirPlayer2 == "East"):
        flip_axis2 = True
        fax2 = 32
        fay2 = 72
    if (dirPlayer2 == "West"):
        flip_axis2 = False
        fax2 = 24
        fay2 = 72
    
    # go up for player 1
    if (pyxel.btn(pyxel.KEY_UP)):
        yPlayer1 -= 1 * global_speed
    # go down for player 1
    if (pyxel.btn(pyxel.KEY_DOWN)):
        yPlayer1 += 1 * global_speed
    # go right for player 1
    if (pyxel.btn(pyxel.KEY_RIGHT)):
        dirPlayer1 = "East"
        xPlayer1 += 1 * global_speed
    # go left for player 1
    if (pyxel.btn(pyxel.KEY_LEFT)):
        dirPlayer1 = "West"
        xPlayer1 -= 1 * global_speed
    # attack for player 1
    if (pyxel.btnp(pyxel.KEY_KP_0)):
        xBulletPlayer1 = xPlayer1
        yBulletPlayer1 = yPlayer1 - 4
        gravity1(dirPlayer1)
        #^^^^^^animation here^^^^^^
        if((pyxel.pget(ctr("PLAYER_1", "x"), ctr("PLAYER_1", "y")) == 2) or (pyxel.pget(ctl("PLAYER_1", "x"), ctl("PLAYER_1", "y")) == 2) or (pyxel.pget(cbr("PLAYER_1", "x"), cbr("PLAYER_1", "y")) == 2) or (pyxel.pget(cbl("PLAYER_1", "x"), cbl("PLAYER_1", "y")) == 2)):
                punch("PLAYER_2")
        
    # go up for player 2
    if (pyxel.btn(pyxel.KEY_Z)):
        yPlayer2 -= 1 * global_speed
    # go down for player 2
    if (pyxel.btn(pyxel.KEY_S)):
        yPlayer2 += 1 * global_speed
    # go right for player 2
    if (pyxel.btn(pyxel.KEY_D)):
        dirPlayer2 = "East"
        xPlayer2 += 1 * global_speed
    # go left for player 2
    if (pyxel.btn(pyxel.KEY_Q)):
        dirPlayer2 = "West"
        xPlayer2 -= 1 * global_speed
    # punch for player 2
    if (pyxel.btnp(pyxel.KEY_SPACE)):
        xBulletPlayer2 = xPlayer2
        yBulletPlayer2 = yPlayer2 - 4
        gravity2(dirPlayer2)
         #^^^^^^animation here^^^^^^
        if( (pyxel.pget(ctr("PLAYER_2", "x"), ctr("PLAYER_2", "y")) == 1) or (pyxel.pget(ctl("PLAYER_2", "x"), ctl("PLAYER_2", "y")) == 1) or (pyxel.pget(cbr("PLAYER_2", "x"), cbr("PLAYER_2", "y")) == 1) or (pyxel.pget(cbl("PLAYER_2", "x"), cbl("PLAYER_2", "y")) == 1)):
                punch("PLAYER_1")
    
    if((pyxel.pget(ctr2("PLAYER_1", "x"), ctr2("PLAYER_1", "y")) == 0) or (pyxel.pget(ctl2("PLAYER_1", "x"), ctl2("PLAYER_1", "y")) == 0) or (pyxel.pget(cbr2("PLAYER_1", "x"), cbr2("PLAYER_1", "y")) == 0) or (pyxel.pget(cbl2("PLAYER_1", "x"), cbl2("PLAYER_1", "y")) == 0)):
            void("PLAYER_1")
            
    if( (pyxel.pget(ctr2("PLAYER_2", "x"), ctr2("PLAYER_2", "y")) == 0) or (pyxel.pget(ctl2("PLAYER_2", "x"), ctl2("PLAYER_2", "y")) == 0) or (pyxel.pget(cbr2("PLAYER_2", "x"), cbr2("PLAYER_2", "y")) == 0) or (pyxel.pget(cbl2("PLAYER_2", "x"), cbl2("PLAYER_2", "y")) == 0)):
            void("PLAYER_2")
       
# show characters with draw()
def draw():
    global factorPlayer1, factorPlayer2, xPlayer1, yPlayer1, xPlayer2, yPlayer2
    
    pyxel.cls(0)
    pyxel.bltm(0, 0, 0, 0, 0, 128, 128)
    pyxel.blt(xPlayer1, yPlayer1, 0, fax1, fay1, factorPlayer1*8, factorPlayer1*8, pyxel.COLOR_BLACK)
    pyxel.blt(xPlayer2, yPlayer2, 0, fax2, fay2, factorPlayer2*8, factorPlayer2*8, pyxel.COLOR_BLACK)
    pyxel.blt(xBulletPlayer1, yBulletPlayer1, 0, faxb1, fayb1, factorPlayer1*8, factorPlayer1*8, pyxel.COLOR_BLACK)
    pyxel.blt(xBulletPlayer2, yBulletPlayer2, 0, faxb2, fayb2, factorPlayer2*8, factorPlayer2*8, pyxel.COLOR_BLACK)
    
# attack function
def punch(player):
    
    global factorPlayer1, factorPlayer2, xPlayer1, xPlayer2
    
    if (player == "PLAYER_2"):
        factorPlayer2 -= 0.2 * factorPlayer1
        factorPlayer1 += 0.1
        xPlayer2 -= 5
    if (player == "PLAYER_1"):
        factorPlayer1 -= 0.2 * factorPlayer2
        factorPlayer2 += 0.1
        xPlayer1 -= 5

# run game
pyxel.run(update, draw)
# update screen
pyxel.show()
