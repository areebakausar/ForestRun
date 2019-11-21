#Areeba Kausar (ak3rej) and Faiz Khan (fk6jr)

# Game Idea: Multiplayer Race taking place

# Required Features:

# User Input: Two players will be laying the game, one will use w and s keys,
# other will use and up and down arrow. Game will start with pressing of spacebar

# Graphics/Images spritesheet of two characters will be inserted who will be running
# through the game

# Start Screen will be built using camera. It will disappear once spacebar is hit

# window size: gamebox.Camera(600, 400) will be implemented

# Optional Features:

#Two players: Move through an obstacle course, starting from opposite sides of the
# screen and working to reach the middle first

#Collectibles
#Power- ups are spread around the course, and users collect them to help them win
#Super speed→ allows player to speed through the obstacle course
# Teleportation→ if you collect this power-up you mover to a further point in the game
# Time saver→ takes 3 or 4 seconds off the players timer

#Timer: In the corner, counts each of the players individual times
# Determines winner in the end

# Health bar:
# If player hits the boundary, they lose a life
# Boundaries are spaced close at some points and farther at others making it more
# difficult to navigate through the maze

#Save points
# Can run multiple races where best out of 3 races wins the tournament
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
walls=[outer1,outer2,outer3,outer4,divider]
#Movement of Players
p1=gamebox.from_color(15,15,'yellow',10,10)
p2=gamebox.from_color(785,15,'yellow',10,10)
players=[p1,p2]
def handle_keys(keys):
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

#Physics of Movement


#Interactives: power ups


#Timers


#Drawing
def tick(keys):
    camera.clear('black')


camera.draw(outer1)
camera.draw(outer2)
camera.draw(outer3)
camera.draw(outer4)
camera.draw(divider)
camera.display()

gamebox.timer_loop(30,tick)





