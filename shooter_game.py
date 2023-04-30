#Создай собственный Шутер!
from pygame import *
from random import randint
 
 
window = display.set_mode((700,500))
display.set_caption('cago')
 
font.init()
font1 = font.SysFont('Arial', 36)
font2 = font.SysFont('Arial', 100)
lost = 0
live = 0
 
 
#mixer.init()
#mixer.music.load('space.ogg')
#mixer.music.play()
 
clock = time.Clock()
FPS = 120
 
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def move(self):
        if key_pressed[K_d] and self.rect.x <=600:
            self.rect.x += self.speed
        if key_pressed[K_a] and self.rect.x >=5:
            self.rect.x -= self.speed
    def update(self):
        global lost
        global live 
        self.rect.y += self.speed
        if self.rect.y > 300:
            self.rect.y = 0
            self.rect.x = randint(30,605)
            self.speed = randint(1,5)
            lost += 1
        grcoll = sprite.groupcollide(bullets, UFO, True, True)
        for el in grcoll:
            live +=1
            ufo6 = GameSprite('ufo.png',randint(30,605), 0 , 65, 65, randint(1,5))
            UFO.add(ufo6)
 
    def fire(self):
        bullet = Bullet('bullet.png',self.rect.centerx, self.rect.top ,15, 20, 5)
        bullets.add(bullet)
 
class Bullet(GameSprite):
    def update(self):
        global live
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
        grcoll = sprite.groupcollide(bullets, UFO, True, True)
        for el in grcoll:
            live += 1
            ufo6 = GameSprite('ufo.png',randint(30,605), 0 , 65, 65, randint(1,5))
            UFO.add(ufo6)

class Asteroids(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(30,605)
            self.speed = randint(1,5) 

rocket = GameSprite('rocket.png', 600, 400, 100, 100,10)
ufo1 = GameSprite('ufo.png',randint(30,605), 0 , 65, 65, randint(5,10))
ufo2 = GameSprite('ufo.png',randint(30,605), 0 , 65, 65, randint(5,10))
ufo3= GameSprite('ufo.png',randint(30,605), 0 , 65, 65, randint(5,10))
ufo4 = GameSprite('ufo.png',randint(30,605), 0 , 65, 65, randint(5,10))
ufo5 = GameSprite('ufo.png',randint(30,605), 0 , 65, 65, randint(5,10))
eew = Asteroids('asteroid.png',randint(30,605), 0 , 65, 65, randint(5,10))
eew2 = Asteroids('asteroid.png',randint(30,605), 0 , 65, 65, randint(5,10))
eew3 = Asteroids('asteroid.png',randint(30,605), 0 , 65, 65, randint(5,10))
bagr = transform.scale(image.load('galaxy.jpg'),(700,500))
 
bullets = sprite.Group()
 
asteroinds = sprite.Group()
asteroinds.add(eew,eew2,eew3)

UFO = sprite.Group()
UFO.add(ufo1,ufo2, ufo3, ufo4, ufo5)
 
game = True
finish = True
 
while game:
    key_pressed = key.get_pressed()
    for i in event.get():
 
        if i.type == QUIT:
            game = False
        elif key_pressed[K_SPACE]:
            rocket.fire()
    if finish == True:
 
        window.blit(bagr , (0,0))
        text_lose1 = font1.render('Пропущено: ' + str(lost), 1, (255,255,255))
        text_lose2 = font1.render('Убиты: ' + str(live), 1, (255,255,255))
        window.blit(text_lose1, (0, 0))
        window.blit(text_lose2, (0, 36))
        rocket.reset()
        bullets.draw(window)
        bullets.update()
        UFO.draw(window)
        UFO.update()
        asteroinds.draw(window)
        asteroinds.update()
 
        if live >= 26:
            text_lose3 = font2.render('Ты победил' , 1, (255,255,255))
            window.blit(text_lose3, (250, 250))
            finish = False
        if lost >= 26:
            text_lose4 = font2.render('YOU LOSE' , 1, (255,255,255))
            window.blit(text_lose4, (250, 250))
            finish = False
 
 
        rocket.move()
 
    clock.tick(FPS)
    display.update() 
    time.delay(20)