#Areeba Kausar (ak3rej) and Faiz Khan (fk6jr)

# Game Idea: Multiplayer Race taking place
import pygame
import gamebox

#Start Screen & Background
camera = gamebox.Camera(800, 600)



#Boundaries/walls
outer1=gamebox.from_color(400,0,'red',800,20)
outer2=gamebox.from_color(0,300,'red',20,600)
outer3=gamebox.from_color(400,600,'red',800,20)
outer4=gamebox.from_color(800,300,'red',20,600)
divider=gamebox.from_color(400,300,'red',10,600)
inner1=gamebox.from_color(160,70,'red',340,8)
inner2=gamebox.from_color(640,70,'red',340,8)
inner3=gamebox.from_color(570,140,'red',340,8)
inner4=gamebox.from_color(640,210,'red',340,8)
inner5=gamebox.from_color(570,280,'red',340,8)
inner6=gamebox.from_color(640,350,'red',340,8)
inner7=gamebox.from_color(570,420,'red',340,8)
inner8=gamebox.from_color(640,490,'red',340,8)
inner9=gamebox.from_color(230,140,'red',340,8)
inner10=gamebox.from_color(160,210,'red',340,8)
inner12=gamebox.from_color(230,280,'red',340,8)
inner13=gamebox.from_color(160,350,'red',340,8)
inner14=gamebox.from_color(230,420,'red',340,8)
inner15=gamebox.from_color(160,490,'red',340,8)

walls=[outer1,outer2,outer3,outer4,divider,inner1,inner2,inner3,inner4,inner5,inner6,inner7,inner8,
       inner9,inner10,inner12,inner13,inner14,inner15]


#Movement of Players
p1=gamebox.from_color(30,40,'yellow',10,10)
p2=gamebox.from_color(770,40,'yellow',10,10)
players=[p1,p2]
def move_players(keys):
  if pygame.K_RIGHT in keys:
    p2.x += 5
  if pygame.K_LEFT in keys:
    p2.x -= 5
  if pygame.K_UP in keys:
    p2.y -= 5
  if pygame.K_DOWN in keys:
    p2.y += 5
  if pygame.K_d in keys:
    p1.x += 5
  if pygame.K_a in keys:
    p1.x -= 5
  if pygame.K_w in keys:
    p1.y -= 5
  if pygame.K_s in keys:
    p1.y += 5

def draw_players(keys):
    move_players(keys)
    for wall in walls:
        for player in players:
            player.move_to_stop_overlapping(wall)
    for player in players:
        camera.draw(player)
#Physics of Movement


#Interactives: power ups


#Timers

def draw_walls():
    for box in walls:
        camera.draw(box)

#Drawing
def tick(keys):
    camera.clear('black')
    draw_walls()
    draw_players(keys)

    camera.display()



gamebox.timer_loop(30,tick)

