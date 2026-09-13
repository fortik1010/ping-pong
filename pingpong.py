from pygame import *

font.init()
window = display.set_mode((700, 500))
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, scale_x, scale_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (scale_x, scale_y))
        self.player_speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_player1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.player_speed
        if keys[K_s] and self.rect.y < 500 - 120:
            self.rect.y += self.player_speed
    def update_player2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.player_speed
        if keys[K_DOWN] and self.rect.y < 500 - 120:
            self.rect.y += self.player_speed
    


player1 = Player('racket.png', 15, 10, 10, 50, 120)
player2 = Player('racket.png', 635, 10, 10, 50, 120)
ball = GameSprite('tenis-ball.png', 350, 250, 3, 55, 55)
font1 = font.Font(None, 50)
speed_y = 5
speed_x = 5

game = True
while game:
    display.update()
    window.fill((100, 100, 255))
    clock.tick(40)
    ball.rect.y += speed_y
    ball.rect.x += speed_x
    if ball.rect.y >= 500-55:
        speed_y *= -1
    if ball.rect.y <= 0:
        speed_y *= -1
    if sprite.collide_rect(ball, player1):
        speed_x *= -1
    if sprite.collide_rect(ball, player2):
        speed_x *= -1
    if ball.rect.x > 700-55:
        window.blit(font1.render('Player 2 lose!', True, (255, 0, 0)), (250, 250))
    if ball.rect.x < 0-55:
        window.blit(font1.render('Player 1 lose!', True, (255, 0, 0)), (250, 250))
    for e in event.get():
        if e.type == QUIT:
            game = False      
    player1.reset()
    player1.update_player1()
    player2.reset()
    player2.update_player2()
    ball.reset()
