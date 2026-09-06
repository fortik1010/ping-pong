from pygame import *
window = display.set_mode((700, 500))
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
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.player_speed
        if keys[K_RIGHT] and self.rect.x < 700 - 100:
            self.rect.x += self.player_speed
    def shoot(self):
        bullet1 = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 10, 10)
        bullets.add(bullet1)
        
game = True
while game:
    window.fill((100, 100, 255))
    for e in event.get():
        if e.type == QUIT:
            game = False      
    display.update()
