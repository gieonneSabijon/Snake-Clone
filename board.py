import pygame
import time
import random
class Snake():
    def __init__(self, x, y):
        self.direction = 3 #  1 = Up / 2 = Down / 3 = Right / 4 = Left
        self.head = (x, y)
        self.tail = []
        self.startTime = time.time()
        self.xIncrement = 25
        self.yIncrement = 0
        self.alive = True

    def move(self):
        if not self.alive:
            self.dying()
            return
        keyPressed = pygame.key.get_pressed()
        if keyPressed[pygame.K_w] and (self.yIncrement != 25 or len(self.tail) == 0):
            self.yIncrement = -25
            self.xIncrement = 0

        elif keyPressed[pygame.K_s] and (self.yIncrement != -25 or len(self.tail) == 0):
            self.yIncrement = 25
            self.xIncrement = 0

        elif keyPressed[pygame.K_d] and (self.xIncrement != -25 or len(self.tail) == 0):
            self.yIncrement = 0
            self.xIncrement = 25

        elif keyPressed[pygame.K_a] and (self.xIncrement != 25 or len(self.tail) == 0):
            self.yIncrement = 0
            self.xIncrement = -25

        endTime = time.time()
        if endTime > self.startTime + 0.15:
            self.startTime = endTime
            if len(self.tail) > 0:
                for i in range(len(self.tail) - 1, 0, -1):
                    self.tail[i] = self.tail[i - 1]
                self.tail[0] = self.head

            self.head = (self.head[0] + self.xIncrement , self.head[1] + self.yIncrement)

    def grow(self):
        if len(self.tail) > 0:
            self.tail.append(self.tail[-1])
        else:
            self.tail.append(self.head)

    def isHit(self):
        headRect = self.render(1)
        playArea = pygame.Rect(0, 0, 615, 460)
        if not pygame.Rect.colliderect(headRect, playArea):
            self.alive = False
            return
        tailList = self.render(0)
        for i, j in enumerate(tailList):
            if pygame.Rect.colliderect(headRect, j) and i != 0:
                self.alive = False

    def dying(self):
        if len(self.tail) > 0:
            endTime = time.time()
            if endTime > self.startTime + 0.01 * -len(self.tail):
                self.startTime = endTime
                self.tail.pop()
        else:
            self.head = (-100,-100)

    def render(self, headOrTail):
        headRect = pygame.Rect(self.head, (25,25))
        tailRect = []
        for i in self.tail:
            tailRect.append(pygame.Rect(i, (25,25)))
        if headOrTail == 1:
            return headRect
        return tailRect

class Apple:
    def __init__(self, snake):
        x, y = random.randint(1, 24) * 25 + 5, random.randint(1, 17) * 25 + 5
        if len(snake.tail) < 408:
            while (x, y) == snake.head or (x, y) in snake.tail:
                x = random.randint(1, 24) * 25 + 5
                y = random.randint(1, 17) * 25 + 5

        self.coords = (x, y)

    def isEaten(self, snake):
        if pygame.Rect.colliderect(pygame.Rect(self.coords, (25,25)), pygame.Rect(snake.head, (25, 25))):
            snake.grow()
            return True
        return False

    def render(self):
        return pygame.Rect(self.coords, (25,25))