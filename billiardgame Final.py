import pygame
import sys
import math
import random

pygame.init()
pygame.mouse.set_visible(True)
font = pygame.font.Font("freesansbold.ttf", 32)


clock = pygame.time.Clock()
window = pygame.display.set_mode([800,600])
background_color = pygame.Color(0,100,0)

class Table:
    def __init__(self):
        self.TableRect = pygame.Rect  (50, 50, 700, 480)
##        self.TableRect.topleft 
##        self.TableRect.topright
##        self.TableRect.bottomleft
##        self.TableRect.bottomright
        
        
        self.color = (0,0,0)
    
        self.x = 60
        self.y = 60
        self.size = 35
    def draw (self, window):
        pygame.draw.rect (window, pygame.Color ("White"), self.TableRect, 4)
        pygame.draw.circle(window, background_color, [self.x, self.y], self.size)
        pygame.draw.circle(window, background_color, [740,59], self.size)
        pygame.draw.circle(window, background_color, [60,521], self.size)
        pygame.draw.circle(window, background_color, [740,523], self.size)

                
    def  CheckCollisions(self, ball):
        ##check top
        if (ball.y - ball.size < self.TableRect.top):
            ball.velocity_y *= -1
            ball.y = self.TableRect.top + ball.size

        ##check left
        if (ball.x - ball.size <self.TableRect.left):
            ball.velocity_x *= -1
            ball.x = self.TableRect.left + ball.size

        ##check right
        if (ball.x + ball.size > self.TableRect.right):
            ball.velocity_x *= -1
            ball.x = self.TableRect.right - ball.size
        ##check bottom
        if (ball.y + ball.size >self.TableRect.bottom):
            ball.velocity_y *= -1
            ball.y = self.TableRect.bottom - ball.size

    def CheckBallCollision(self, pocket, ball, pocket_size):
        
        #move to origin
        origin_x = pocket[0] - ball.x
        origin_y = pocket[1] - ball.y
        
        #get distance between circles
        distance = math.sqrt((origin_x * origin_x) + (origin_y * origin_y))

        #check if ball is inside pocket
        if (distance < pocket_size):
            return True
        else:
            return False

    def Update(self, list_of_balls):
        for ball in list_of_balls:
            if (self.CheckBallCollision([60, 60], ball, self.size) or \
                self.CheckBallCollision([740,59], ball, self.size) or \
                self.CheckBallCollision([60, 521], ball, self.size) or \
                self.CheckBallCollision([740, 523], ball, self.size)):

                list_of_balls.remove(ball)
    
        
        

        

     
            

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity_x = 0
        self.velocity_y = 0
        self.size = 15
        self.color = pygame.Color(0,0,0)

    def update(self):
        
        self.x += self.velocity_x
        self.y += self.velocity_y

        self.velocity_x *= 0.99
        self.velocity_y *= 0.99

        self.x = int(self.x)
        self.y = int(self.y)

        if (self.x > 800):
            self.velocity_x *=-1
        if (self.x < 0):
            self.velocity_x = self.velocity_x * -1

        if (self.y < 0):
            self.velocity_y *=-1
        if (self.y > 600):
            self.velocity_y *=-1
        
    def draw(self, window):
        pygame.draw.circle(window, self.color, [self.x, self.y], self.size)

def checkcollision (ball1, ball2):
    origin_x = ball2.x- ball1.x
    origin_y = ball2.y- ball1.y
    distance = (origin_x * origin_x)+ (origin_y * origin_y)
    combined_radius = (ball1 .size + ball2.size)
    circle_distance = combined_radius * combined_radius
    return (distance <= circle_distance)



def CollideReaction (ball1, ball2):
    #move to origin
        origin_x = ball2.x - ball1.x
        origin_y = ball2.y - ball1.y

        #find distance to origin (pythagorean)
        distance = math.sqrt(origin_x * origin_x + origin_y * origin_y)

        if (distance == 0):
            distance = 1

        #normalize
        normal_x = origin_x / distance
        normal_y = origin_y / distance

        #invert normal
        #normal_mouse_x *=-1
        #normal_mouse_y *=-1
         #move ball away from cursor, using the inverted normal


        #apply velocities
        #ball1 transfers its velocity to ball2
        ball2.velocity_x = ball1.velocity_x * normal_x
        ball2.velocity_y = ball1.velocity_y* normal_y


        #reflect ball1 (iverted velocity)
        ball1.velocity_x *=  -normal_x
        ball1.velocity_y *= -normal_y

        ball1.update()
        ball2.update()
        


list_of_balls = [Ball(400,300),Ball(430, 320), Ball(430, 280), Ball(460, 260), Ball(460, 300), Ball(460, 340)] ##    ,Ball(65,70),Ball(735,70),Ball(70,515),Ball(735,515)]
list_of_balls = list_of_balls
                 
mother_ball = Ball(80,300)
mother_ball.color = pygame.Color(255,255,255)
mother_ball.size = 15




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill(background_color)

    mouse_pos = pygame.mouse.get_pos()
    msg = "%i %i" %(mouse_pos[0],mouse_pos[1])
    text = font .render(msg, False, pygame.Color(0,0,0))
    window.blit(text,[0,0])

    if (pygame.mouse.get_pressed()[0] == True):
##        for ball in list_of_balls:
##            #move to origin
##            origin_mouse_x = mouse_pos[0] - ball.x
##            origin_mouse_y = mouse_pos[1] - ball.y
##            #find distance to origin (pythagorean)
##            distance = math.sqrt(origin_mouse_x * origin_mouse_x + origin_mouse_y * origin_mouse_y)
##
##            #normalize
##            normal_mouse_x = origin_mouse_x / distance
##            normal_mouse_y = origin_mouse_y / distance
##
##            #invert normal
##            #normal_mouse_x *=-1
##            #normal_mouse_y *=-1
##
##            #move ball away from cursor, using the inverted normal
##            ball.velocity_x += normal_mouse_x * 2.5
##            ball.velocity_y += normal_mouse_y * 2.5
##

            #move to origin
                origin_mouse_x = mouse_pos[0] -mother_ball.x
                origin_mouse_y = mouse_pos[1] - mother_ball.y
            #find distance to origin (pythagorean)
                distance = math.sqrt(origin_mouse_x * origin_mouse_x + origin_mouse_y * origin_mouse_y)

            #normalize
                normal_mouse_x = origin_mouse_x / distance
                normal_mouse_y = origin_mouse_y / distance

            #invert normal
                normal_mouse_x *=-1
                normal_mouse_y *=-1

            #move ball away from cursor, using the inverted normal
                mother_ball.velocity_x += normal_mouse_x * 2.5
                mother_ball.velocity_y += normal_mouse_y * 2.5

    PoolTable = Table ()

    PoolTable.draw(window)
    for ball in list_of_balls:    
        ball.update()
        ball.draw(window)
        
        
    
        if (checkcollision (mother_ball, ball) == True):
            CollideReaction(mother_ball, ball)


    for ball1 in list_of_balls:
        for ball2 in list_of_balls:
            if (ball1 != ball2):
                if (checkcollision (ball1, ball2)):
                    CollideReaction(ball1, ball2)

    PoolTable.CheckCollisions (mother_ball)

    
    PoolTable.Update(list_of_balls)

    for ball in list_of_balls:
        PoolTable.CheckCollisions(ball)

  
                            
    mother_ball.update()
    mother_ball.draw(window)

    pygame.display.update()
    clock.tick(30)
