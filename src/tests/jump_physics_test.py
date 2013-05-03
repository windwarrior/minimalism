#!/usr/bin/python2.7

import pygame
from pygame.locals import *

class JumpPhysicsTest(object):
    def __init__(self):
        self.size = (640, 480)
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.clock = pygame.time.Clock()
        self.player = Player()

    def process_event(self, event):
        if event.type == QUIT:
            self._running = False
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                self.player.jump()

            if event.key == K_LEFT:
                self.player.goLeft = True
            elif event.key == K_RIGHT:
                self.player.goRight = True

        elif event.type == KEYUP:
            if event.key == K_LEFT:
                self.player.goLeft = False
            elif event.key == K_RIGHT:
                self.player.goRight = False

    def update_entities(self):
        self.player.update()

    def render(self):
        self._display_surf.fill(pygame.Color("black"))
        pygame.draw.line(self._display_surf, pygame.Color("white"), (5, 440), (635, 440), 1)
        pygame.draw.rect(self._display_surf, pygame.Color("green"), (5, 5, 630, 470), 1)

        pygame.draw.rect(self._display_surf, pygame.Color("red"), self.player.get_rect(), 1)
        pygame.display.update()

    def run(self):
        while(self._running):
            for event in pygame.event.get():
                self.process_event(event)
            self.update_entities()
            self.render()
            self.clock.tick(30)


class Player(object):
    def __init__(self):
        self.pos_x = 20
        self.pos_y = 420
        self.height = 40
        self.width = 20
        self.max_x_vel = 10
        self.max_y_vel = 20
        self.velocity = (0.0, 0.0)
        self.jumping = False
        self.goLeft = False
        self.goRight = False

    def jump(self):
        if not self.jumping:
            (oldXvel, oldYvel) = self.velocity
            self.velocity = (oldXvel, -self.max_y_vel)
            self.jumping = True

    def update(self):
        (velX, velY) = self.velocity

        # X positie aanpassen aan de hand van de ingedrukte toets
        self.pos_x = self.pos_x + velX

        # X velocity van de speler aanpassen, linear
        # in deze situatie kan de speler in de lucht bewegen
        if self.goRight:
            self.max_x_vel = 4 if self.jumping and velX < 0 else self.max_x_vel
            velX = min(self.max_x_vel, velX + 1)
        elif self.goLeft:
            self.max_x_vel = 4 if self.jumping and velX > 0 else self.max_x_vel
            velX = max(-self.max_x_vel, velX - 1)
        else:
            if velX > 0:
                velX = max(0, velX - 1)
            else:
                velX = min(0, velX + 1)

        # X positie "collision detection, niet zoals het hoort, maar voor deze demo
        # genoeg

        if self.pos_x > 625:
            self.pos_x = 625
            velX = 0
        elif self.pos_x < 15:
            self.pos_x = 15
            velX = 0

        # Y positie aanpassen naar mate velocity
        self.pos_y =  self.pos_y + velY
    
        # Y collision detection, als de player weer op de grond staat is hij niet aan
        # het springen
        if(self.pos_y > 420):
            self.pos_y = 420
            self.jumping = False
            self.velocity = (velX, 0)
            self.max_x_vel = 10

        # Y velocity aanpassen aan de hand van of de speler springt of niet
        # in dit geval linear
        self.velocity = (velX, min(velY + 1, self.max_y_vel) if self.jumping else velY)
         
    
    def get_rect(self):
        xmin = self.pos_x - self.width / 2
        ymin = self.pos_y - self.height / 2
        return (xmin, ymin, self.width, self.height)
        

if __name__ == "__main__":
    jp = JumpPhysicsTest()
    jp.run()

