import pgzrun

WIDTH = 800
HEIGHT = 600
class AnimatedSprite:
    def __init__(self, x, y, images, speed=5):
        self.actor = Actor(images[0])
        self.x = x
        self.y = y
        self.images = images
        self.speed = speed
        self.frame = 0
        self.counter = 0

    def draw(self):
        self.actor.draw()

    def update(self):
        self.counter += 1
        if self.counter % self.speed == 0:
            self.frame = (self.frame + 1) % len(self.images) # Обновляем actor только если текущий кадр первый или их всего один
            self.actor.image = self.images[self.frame]  # Используем load_image для обновления изображения актера

player_images = ['player1', 'player2', 'player3', 'player4', 'player5']
enemy_images = ['enemy1', 'enemy2', 'enemy3', 'enemy4', 'enemy5']

playerPos = [0, 1]
enemy1Pos = [500, 100]
enemy2Pos = [600,100]
player = AnimatedSprite(playerPos[0], playerPos[1], player_images, 10)
enemy1 = AnimatedSprite(enemy1Pos[0], enemy1Pos[1], enemy_images, 10)
enemy2 = AnimatedSprite(enemy2Pos[0], enemy2Pos[1], enemy_images, 10)
player.actor.pos = playerPos[0], playerPos[1]
enemy1.actor.pos = enemy1Pos[0], enemy1Pos[1]
enemy2.actor.pos = enemy2Pos[0], enemy2Pos[1]

SPEED = 12
GRAVITY = 10

getStarted = Actor('getstarted')
soundsOn = Actor('sounds')
exit = Actor('exit')
level1 = Actor('level')
level2 = Actor('level')

Level1 = [100, 200]
Level2 = [WIDTH-300, 300]
level1.pos = Level1[0], Level1[1]
level2.pos = Level2[0], Level2[1]
getStarted.pos = WIDTH/2, HEIGHT/2-25
soundsOn.pos = WIDTH/2, HEIGHT/2
exit.pos = WIDTH/2, HEIGHT/2+25

menuTrig = 0
notDown = 0
movingCount1 = 0
movingCount2 = 0
moveAgain1 = 0
moveAgain2 = 0
def draw():
    screen.clear()
    if menuTrig == 0:
        getStarted.draw()
        exit.draw()
        soundsOn.draw()
    else:
        screen.blit('background', (0, 0))
        level1.draw()
        level2.draw()
        player.actor.draw()
        if enemy1:
            enemy1.actor.draw()
        if enemy2:
            enemy2.actor.draw()



def update():
    global GRAVITY
    global notDown
    global movingCount1
    global movingCount2
    global moveAgain1
    global moveAgain2
    if menuTrig == 1:
        if enemy1:
            if movingCount1 < 100 and moveAgain1 == 0:
                enemy1.actor.left += 5
                movingCount1 += 5
                enemy1.update()
                if movingCount1 == 100:
                    moveAgain1 = 1
            elif moveAgain1 == 1:
                enemy1.actor.left -= 5
                movingCount1 -= 5
                enemy1.update()
                if movingCount1 == 0:
                    moveAgain1 = 0
            if not (enemy1.actor.colliderect(level1)) and not (enemy1.actor.colliderect(level2)):
                enemy1.actor.top += GRAVITY
                enemy1Pos[1] += GRAVITY
            else:
                enemy1.actor.left += 5
                enemy1.actor.left -= 5
        if enemy2:
            if movingCount2 < 150 and moveAgain2 == 0:
                enemy2.actor.left -= 5
                movingCount2 += 5
                enemy2.update()
                if movingCount2 == 150:
                    moveAgain2 = 1
            elif moveAgain2 == 1:
                enemy2.actor.left += 5
                movingCount2 -= 5
                enemy2.update()
                if movingCount2 == 0:
                    moveAgain2 = 0
            if not (enemy2.actor.colliderect(level1)) and not (enemy2.actor.colliderect(level2)):
                enemy2.actor.top += GRAVITY
                enemy2Pos[1] += GRAVITY
            else:
                enemy2.actor.left += 5
                enemy2.actor.left -= 5
        if keyboard.d:
            player.actor.left += SPEED
            playerPos[0] += SPEED
            player.update()
        if keyboard.a:
            player.actor.left -= SPEED
            playerPos[0] -= SPEED
            player.update()
        if not(player.actor.colliderect(level1)) and not(player.actor.colliderect(level2)):
            player.actor.top += GRAVITY
            playerPos[1] += GRAVITY
        else:
            if keyboard.a or keyboard.d:
                sounds.footstep.play()
            notDown = 1

def on_key_down(key):
    global enemy1
    global enemy2
    if menuTrig == 1:
        if key == 115 and notDown == 0:
            player.actor.top += SPEED
            playerPos[1] += SPEED
        if key == 119:
            player.actor.top -= 100
            playerPos[1] -= 100
        if key == 102:
            if enemy1 and player.actor.colliderect(enemy1.actor):
                enemy1 = 0
            elif enemy2 and player.actor.colliderect(enemy2.actor):
                enemy2 = 0


def on_mouse_down(pos):
    global menuTrig
    if getStarted.collidepoint(pos):
        print("Игра началась")
        menuTrig = 1
    elif soundsOn.collidepoint(pos):
        print("Звук включен")
    elif exit.collidepoint(pos):
        exit()


pgzrun.go()