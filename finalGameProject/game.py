#Areeba Kausar (ak3rej) and Faiz Khan (fk6jr)

# Game Idea: Multiplayer Race taking place
import pygame
import gamebox
import random

#Start Screen & Background
camera = gamebox.Camera(800, 600)
#lives
p1_lives = 3
p2_lives = 3
p1_score = 0
p2_score = 0
timer = 10000

#Boundaries/walls
outer1=gamebox.from_color(400,100,'tomato',800,5)
outer2=gamebox.from_color(00,350,'tomato',10,500)
outer3=gamebox.from_color(400,600,'tomato',800,10)
outer4=gamebox.from_color(800,350,'tomato',10,500)
divider=gamebox.from_color(400,350,'tomato',10,500)
inner1=gamebox.from_color(230,550,'violet',340,8)
inner2=gamebox.from_color(570,550,'violet',340,8)
inner3=gamebox.from_color(570,150,'peachpuff',340,8)
inner4=gamebox.from_color(640,210,'sandybrown',340,8)
inner5=gamebox.from_color(570,280,'gold',340,8)
inner6=gamebox.from_color(640,350,'turquoise',340,8)
inner7=gamebox.from_color(570,420,'royal blue',340,8)
inner8=gamebox.from_color(640,490,'mediumslateblue',340,8)
inner9=gamebox.from_color(230,150,'peachpuff',340,8)
inner10=gamebox.from_color(160,210,'sandybrown',340,8)
inner12=gamebox.from_color(230,280,'gold',340,8)
inner13=gamebox.from_color(160,350,'turquoise',340,8)
inner14=gamebox.from_color(230,420,'royal blue',340,8)
inner15=gamebox.from_color(160,490,'mediumslateblue',340,8)


walls=[outer1,outer2,outer3,outer4,divider,inner1,inner2,inner3,inner4,inner5,inner6,inner7,inner8,
       inner9,inner10,inner12,inner13,inner14,inner15]

# Creation of Background elements of Bushes
# Implementing required Feature 2: Graphics/Images (You should use some appropriate images in your game):
bush1a = gamebox.from_image(15, 110, "hurdle_bushes.png", )
bush1a.scale_by(0.05)
bush1 = gamebox.from_image(15, 150, "hurdle_bushes.png",)
bush1.scale_by(0.05)
bush1b = gamebox.from_image(15, 200, "hurdle_bushes.png", )
bush1b.scale_by(0.05)

bush2a = gamebox.from_image(15, 225, "hurdle_bushes.png", )
bush2a.scale_by(0.05)
bush2 = gamebox.from_image(15, 280, "hurdle_bushes.png",)
bush2.scale_by(0.05)
bush2b = gamebox.from_image(15, 335, "hurdle_bushes.png", )
bush2b.scale_by(0.05)

bush3a = gamebox.from_image(15, 360, "hurdle_bushes.png", )
bush3a.scale_by(0.05)
bush3 = gamebox.from_image(15, 420, "hurdle_bushes.png",)
bush3.scale_by(0.05)
bush3b = gamebox.from_image(15, 480, "hurdle_bushes.png",)
bush3b.scale_by(0.05)

bush4a = gamebox.from_image(15, 505, "hurdle_bushes.png", )
bush4a.scale_by(0.05)
bush4 = gamebox.from_image(15, 550, "hurdle_bushes.png",)
bush4.scale_by(0.05)
bush4b = gamebox.from_image(15, 590, "hurdle_bushes.png", )
bush4b.scale_by(0.05)

bush5a = gamebox.from_image(785, 110, "hurdle_bushes.png", )
bush5a.scale_by(0.05)
bush5 = gamebox.from_image(785, 150, "hurdle_bushes.png",)
bush5.scale_by(0.05)
bush5b = gamebox.from_image(785, 200, "hurdle_bushes.png", )
bush5b.scale_by(0.05)

bush6a = gamebox.from_image(785, 225, "hurdle_bushes.png", )
bush6a.scale_by(0.05)
bush6 = gamebox.from_image(785, 280, "hurdle_bushes.png",)
bush6.scale_by(0.05)
bush6b = gamebox.from_image(785,335, "hurdle_bushes.png", )
bush6b.scale_by(0.05)

bush7a = gamebox.from_image(785, 360, "hurdle_bushes.png", )
bush7a.scale_by(0.05)
bush7 = gamebox.from_image(785, 420, "hurdle_bushes.png",)
bush7.scale_by(0.05)
bush7b = gamebox.from_image(785, 480, "hurdle_bushes.png", )
bush7b.scale_by(0.05)

bush8a = gamebox.from_image(785, 505, "hurdle_bushes.png", )
bush8a.scale_by(0.05)
bush8 = gamebox.from_image(785, 550, "hurdle_bushes.png",)
bush8.scale_by(0.05)
bush8b = gamebox.from_image(785, 590, "hurdle_bushes.png", )
bush8b.scale_by(0.05)

bushes = [bush1a,bush1b,bush1,bush2a,bush2b,bush2,bush3a,bush3b,bush3,bush4a,bush4b,bush4,bush5a,bush5b,bush5,bush6a,bush6b,bush6,bush7a,bush7b,bush7,bush8a,bush8b,bush8]

# Creation of moving Enemy fire
# characters that can hinder the player character from accomplishing the goal

flame1 = gamebox.from_image(785, 190, "hurdle_flames.png",)
flame1.scale_by(0.02)
flame2 = gamebox.from_image(785, 260, "hurdle_flames.png",)
flame2.scale_by(0.02)
flame3 = gamebox.from_image(785, 330, "hurdle_flames.png",)
flame3.scale_by(0.02)
flame4 = gamebox.from_image(785, 400, "hurdle_flames.png",)
flame4.scale_by(0.02)
flame5 = gamebox.from_image(785, 470, "hurdle_flames.png",)
flame5.scale_by(0.02)
flame6 = gamebox.from_image(785, 530, "hurdle_flames.png",)
flame6.scale_by(0.02)

flame7 = gamebox.from_image(15, 190, "hurdle_flames_2.png",)
flame7.scale_by(0.02)
flame8 = gamebox.from_image(15, 260, "hurdle_flames_2.png",)
flame8.scale_by(0.02)
flame9 = gamebox.from_image(15, 330, "hurdle_flames_2.png",)
flame9.scale_by(0.02)
flame10 = gamebox.from_image(15, 400, "hurdle_flames_2.png",)
flame10.scale_by(0.02)
flame11 = gamebox.from_image(15, 470, "hurdle_flames_2.png",)
flame11.scale_by(0.02)
flame12 = gamebox.from_image(15, 530, "hurdle_flames_2.png",)
flame12.scale_by(0.02)

flames_r = [flame1,flame2,flame3,flame4,flame5,flame6]
flames_l = [flame7,flame8,flame9,flame10,flame11,flame12]
flames = [flame1,flame2,flame3,flame4,flame5,flame6,flame7,flame8,flame9,flame10,flame11,flame12]

#Movement of Players
p1=gamebox.from_color(40,120,'cyan',10,10)
p2=gamebox.from_color(760,120,'lawngreen',10,10)
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
    for bush in bushes:
        for player in players:
            player.move_to_stop_overlapping(bush)
    for player in players:
        camera.draw(player)


#Interactives: power ups


#Timers

# background drawing

def draw_walls():
    for box in walls:
        camera.draw(box)

def draw_bushes():
    global p1_score
    global p2_score
    for bush in bushes:
        camera.draw(bush)
        if p1.touches(bush):
            p1_score -= 1
            p1.move_both_to_stop_overlapping(bush)
        if p2.touches(bush):
            p2_score -= 1
            p2.move_both_to_stop_overlapping(bush)

def draw_flames():
    for flame in flames:
        camera.draw(flame)

def move_flames():
    for flame_r in flames_r:
        flame_r.x -= 3
        if flame_r.x < -15:
            flame_r.x = 785
    for flame_l in flames_l:
        flame_l.x += 3
        if flame_l.x > 815:
            flame_l.x = 15

def draw_lives_p1(num_lives):
    first_x = camera.left+20
    y = camera.top+20
    for i in range(num_lives):
        life = gamebox.from_circle(first_x + i*40, y, 'cyan', 15)
        camera.draw(life)

def draw_lives_p2(num_lives):
    first_x = camera.right-20
    y = camera.top+20
    for i in range(num_lives):
        life = gamebox.from_circle(first_x - i*40, y, 'lawngreen', 15)
        camera.draw(life)

def draw_scorebox():
    score_box_1 = gamebox.from_text(300, camera.top+20, "Player 1 Score: " + str(p1_score), 24, "white")
    camera.draw(score_box_1)
    score_box_2 = gamebox.from_text(500, camera.top+20, "Player 2 Score: " + str(p2_score), 24, "white")
    camera.draw(score_box_2)

#Drawing
game_on = False
game_status = '0'

def tick(keys):
    camera.clear('black')
    global game_on
    global p2_lives
    global p1_lives
    global p1_score
    global p2_score
    global game_status
    global timer

    #Setting Results:

    if p1_lives == 0:
        result = gamebox.from_text(400, 100, "Player 2 Won", 100, 'green', True, False)
        camera.draw(result)
        game_on = False
    if p2_lives == 0:
        result = gamebox.from_text(400, 100, "Player 1 Won", 100, 'green', True, False)
        camera.draw(result)
        game_on = False

    if timer == 0:
       if p2_score == p1_score:
            result = gamebox.from_text(400, 100, "It is a Tie", 100, 'green', True, False)
            camera.draw(result)
            game_on = False
       elif p1_score > p2_score:
           result1 = gamebox.from_text(400, 300, "Player 1 Won", 500, 'green')
           camera.draw(result1)
           game_on = False
       elif p2_score > p1_score:
           result2 = gamebox.from_text(400, 300, "Player 2 Won", 500, 'green')
           camera.draw(result2)
           game_on = False


    if pygame.K_SPACE not in keys and game_on == False and game_status == '0':
        title1 = gamebox.from_text(400, 100, "Forest Run", 100, 'green', True, False)
        title2 = gamebox.from_text(400, 200, "by Faiz Khan (fk6jr) and Areeba Kausar (ak3rej)", 30, 'white',
                                   True, False)
        title3 = gamebox.from_text(400, 300,
                                   "This is a two player game in which players race through a forest.",
                                   24, 'white', False, False)
        title5 = gamebox.from_text(400, 325,"Player 1 (left on screen) will use the WASD keys to move up, left, down, and right respectively.",
                                  24,'white',False,False)
        title6 = gamebox.from_text(400, 350,
                                   "Player 2 (right on screen) will use the arrow keys to move. ",
                                   24, 'white', False, False)
        title7 = gamebox.from_text(400, 375,
                                   "Avoid losing lives by not touching the flames. Avoid Bushes to not lose score",
                                   24, 'white', False, False)
        title8 = gamebox.from_text(400, 400,
                                   "Collect Gems to add to score. ", 24, 'white', False, False)
        title9 = gamebox.from_text(400, 425,
                                   "Winner is the one who collects most points before timer runs out!", 24, 'white', False, False)

        title4 = gamebox.from_text(400, 525,
                                   "Press the space bar to start", 24, 'white', True, False)
        camera.draw(title1)
        camera.draw(title2)
        camera.draw(title3)
        camera.draw(title4)
        camera.draw(title5)
        camera.draw(title6)
        camera.draw(title7)
        camera.draw(title8)
        camera.draw(title9)

    if pygame.K_SPACE in keys:
        game_on = True
        game_status = '1'

    if game_on == True and game_status == '1':
        draw_walls()
        draw_bushes()
        draw_flames()
        move_flames()
        draw_players(keys)
        draw_lives_p1(p1_lives)
        draw_lives_p2(p2_lives)
        draw_scorebox()

        timer_box = gamebox.from_text(400, camera.top + 50, "Time remaining: " + str(timer), 24, "white")
        timer -= 1
        camera.draw(timer_box)

        for flame in flames:
            if p1.touches(flame):
                p1.move_to_stop_overlapping(flame)
                p1_lives -= 1
                p1.center = [40,120]
            if p2.touches(flame):
                p2.move_to_stop_overlapping(flame)
                p2_lives -= 1
                p2.center = [760, 120]

    camera.display()



gamebox.timer_loop(30,tick)
