from random import randrange, randint
import pygame, time, sys, os, threading, random, requests

# Important
assetsloc = "C:\ProgramData\Pong_Game"
font = "C:\ProgramData\Pong_Game\Roboto-Medium.ttf"
iconpath = "C:\ProgramData\Pong_Game\Pong_game_icon_768px.png"
if not os.path.exists(assetsloc): # Downloading assets for game
    os.makedirs(assetsloc)
    url = "https://raw.githubusercontent.com/TMarccci/PongRemastered_Proj/master/assets/Pong_game_icon_768px.png"
    fname = assetsloc + "\Pong_game_icon_768px.png"
    r = requests.get(url)
    open(fname, 'wb').write(r.content)
    
    url2 = "https://raw.githubusercontent.com/TMarccci/PongRemastered_Proj/master/assets/Roboto-Medium.ttf"
    fname2 = assetsloc + "\Roboto-Medium.ttf"
    r2 = requests.get(url2)
    open(fname2, 'wb').write(r2.content)
        
pygame.init() # Running pygame
clock = pygame.time.Clock() # Define tick

# Primary prop
screenW = 1280 # Screen resolution Width
screenH = 960 # Screen resolution Height
screenTitle = "Pong Remastered 99% Veszély!!4!44!!4"
icon = pygame.image.load(iconpath) # Icon import
pygame.display.set_icon(icon) # Icon set
screen = pygame.display.set_mode((screenW, screenH)) # Define screen
pygame.display.set_caption(screenTitle) # Define screen title

# Const vars
ffam = pygame.font.Font(font, 30) # Font type for game
ballspeed_x = ballspeed_y = 5 # Ball speed
waittimeo = 4 # Waittime for ball to start
waittime = waittimeo # Same
settingsdone = False # State
exit = False # State

# Colors
bgcolor = pygame.Color("grey12")
white = (255, 255, 255)
red = (255, 0, 0)
lightgrey = (200, 200, 200)
black = (0, 0, 0)
orange = (255,69,0)
aqua = 	(0,255,255)

# Zero Vars
player1speedup = player1speeddown = player2speedup = player2speeddown = statp1 = statp2 = 0 # Yeah it is just 0
stateofplayermode = stateofbotpups = stateofpupsunblock = "" # And this is nothing

# BOT Settings and Play Mode
pupall = True # Some settings states
pupbot = True # Tho
p1mode = True # Tho
p2speedonBOT = 4.5 # Bot speed

# Power UP Time settings
# P1
randompup1 = True # Selecting powerup to show
pupvis1 = False # State of visible powerups
blocker1 = False # Blocks multithread loop
hiddenw1l = True # Status of timer visibility
hiddens1l = True # -II-
w1enabled = False # Status of the powerup
s1enabled = False # Status of the powerup and function
# P2
randompup2 = True # Selecting powerup to show
pupvis2 = False # State of visible powerups
blocker2 = False # Blocks multithread loop
hiddenw2l = True # Status of timer visibility
hiddens2l = True # -II-
w2enabled = False # Status of the powerup
s2enabled = False # Status of the powerup and function

frominter = 4 # From interval to powerups
tointer = 8 # To interval to powerups
poweruptime = 6 # Duration of the powerup GL
timeleft_w1 = timeleft_s1 = timeleft_w2 = timeleft_s2 = 0 # Setting duration for each

# Elements and their pos
ball = pygame.Rect(screenW/2 - 10, screenH/2 - 10, 20, 20,)
player1 = pygame.Rect(50, screenH/2 - 60, 10, 120)
player2 = pygame.Rect(screenW - 50, screenH/2 - 60, 10, 120)
goal1 = pygame.Rect(-7, 0, 8, screenH)
goal2 = pygame.Rect(screenW - 1, 0, 8, screenH)
powerup1wider = pygame.Rect(50, -20, 10, 10)
speed1powerup = pygame.Rect(50, -20, 10, 10)
powerup2wider = pygame.Rect(screenW - 50, -20, 10, 10)
speed2powerup = pygame.Rect(screenW - 50, -20, 10, 10)

# Exit fc
def exit():
    global exit # Exit state
    exit = True
    
    pygame.quit
    sys.exit()

# Ball fc
def ballfnc():
    global ballspeed_x, ballspeed_y, statp1, statp2, waittime
    
    if waittime == 0:
        # Ball move
        ball.x += ballspeed_x
        ball.y += ballspeed_y

        # Frame for ball and collision
        if ball.left <= 0 or ball.right >= screenW:
            ballspeed_x *= -1
        if ball.top <= 0 or ball.bottom >= screenH:
            ballspeed_y *= -1
        if ball.colliderect(player1) or ball.colliderect(player2):
            ballspeed_x *= -1
        
        # Goal
        if ball.colliderect(goal1):
            # Ball reset
            ball.left = screenW/2 - 10
            ball.top = screenH/2 - 10
            statp1 += 1 # Stat points
            
            # Ball Start Counter
            waittime = waittimeo # Resetting wait time
            thread_wait = threading.Thread(target=ballstart,)
            thread_wait.start() # Start countdown on thread
        elif ball.colliderect(goal2):
            # Ball reset
            ball.left = screenW/2 - 10
            ball.top = screenH/2 - 10
            statp2 += 1 # Stat points
            
            # Ball Start Counter
            waittime = waittimeo # Resetting wait time
            thread_wait = threading.Thread(target=ballstart,)
            thread_wait.start() # Start countdown on thread
def ballstart():
    global waittime, exit
    
    # Wait
    while waittime > 0:
        waittime -= 1
        for i in range(100):
            time.sleep(0.01)
            if exit == True:
                break

# Powerups timeleft fc
# Wide powerup
# P1
def timeleft_w1tl():
    global timeleft_w1, hiddenw1l, poweruptime, w1enabled, exit

    while timeleft_w1 > 0: # Countdown
        timeleft_w1 -= 1
        for i in range(100): # Safesleep
            time.sleep(0.01)
            if exit == True:
                break
    player1.height = 120 # Disableing powerup
    w1enabled = False # Disableing status
    hiddenw1l = True # Hiding timer  
# P2
def timeleft_w2tl():
    global timeleft_w2, hiddenw2l, poweruptime, w2enabled, exit

    while timeleft_w2 > 0: # Countdown
        timeleft_w2 -= 1
        for i in range(100): # Safesleep
            time.sleep(0.01)
            if exit == True:
                break
    player2.height = 120 # Disableing powerup
    w2enabled = False # Disableing status
    hiddenw2l = True # Hiding timer
    
# Speed powerup
# P1
def timeleft_s1tl():
    global timeleft_s1, hiddens1l, poweruptime, s1enabled, exit

    while timeleft_s1 > 0: # Countdown
        timeleft_s1 -= 1
        for i in range(100): # Safesleep
            time.sleep(0.01)
            if exit == True:
                break
    s1enabled = False # Disableing powerup and status
    hiddens1l = True # Hiding timer
# P2
def timeleft_s2tl():
    global timeleft_s2, hiddens2l, poweruptime, s2enabled, exit

    while timeleft_s2 > 0: # Countdown
        timeleft_s2 -= 1
        for i in range(100): # Safesleep
            time.sleep(0.01)
            if exit == True:
                break
    s2enabled = False # Disableing powerup and status
    hiddens2l = True # Hiding timer

# Powerup randoms appear and pos
# P1
def spawncalc1():
    global randompup1, w1enabled, s1enabled, pupvis1, blocker1, exit

    randompup1 = randrange(2) # Select random powerup
    # randompup1 = 0 # For Dev Select only one pup

    if pupvis1 == False: # Check if is there any powerups visible
        blocker1 = True
        for i in range(randint(frominter,tointer)*100): # Calculated spawntime
            time.sleep(0.01) # Safesleep
            if exit == True:
                break
        # Show the selected one (randompup1)
        if randompup1 == 0:
            pupvis1 = True # Some state
            blocker1 = False # -II-
            powerup1wider.y = random.randrange(10, 950)
        elif randompup1 == 1:
            pupvis1 = True # Some state
            blocker1 = False # -II-
            speed1powerup.y = random.randrange(10, 950)
# P2
def spawncalc2():
    global randompup2, w2enabled, s2enabled, pupvis2, blocker2, exit

    randompup2 = randrange(2) # Select random powerup
    # randompup2 = 0 # For Dev Select only one pup

    if pupvis2 == False: # Check if is there any powerups visible
        blocker2 = True
        for i in range(randint(frominter,tointer)*100): # Calculated spawntime
            time.sleep(0.01) # Safesleep
            if exit == True:
                break
        # Show the selected one (randompup2)
        if randompup2 == 0:
            pupvis2 = True # Some state
            blocker2 = False # -II-
            powerup2wider.y = random.randrange(10, 950)
        elif randompup2 == 1:
            pupvis2 = True # Some state
            blocker2 = False # -II-
            speed2powerup.y = random.randrange(10, 950)
                
# Player1
# Movement
def player1fncup():
    global player1speedup

    # Move player by
    player1.y += player1speedup
def player1fncdown():
    global player1speeddown

    # Move player by
    player1.y += player1speeddown
# Props
def player1prop():
    global poweruptime, hiddenw1l, hiddens1l, w1enabled, s1enabled, pupvis1, timeleft_w1, timeleft_s1

    # Preventing leaving from playspace
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= screenH:
        player1.bottom = screenH

    # Touching powerups
    # Wider powerup
    if player1.colliderect(powerup1wider):
        powerup1wider.y = -20 # Hide from screen
        player1.height = 200 # Activate powerup - Wide
        pupvis1 = False # Powerup visible on screen
        w1enabled = True # Activate Status
        hiddenw1l = False # Show timer of the Powerup

        # If you pickup a powerup while you have an anotherone add time to it
        if timeleft_w1 > 0:
            timeleft_w1 += poweruptime # Adding poweruptime to timeleft powerup
        else:
            timeleft_w1 = poweruptime # Resetting powerup timeleft
            thread_w1tl = threading.Thread(target=timeleft_w1tl,)
            thread_w1tl.start() # Start timer and more

    # Speed powerup
    if player1.colliderect(speed1powerup):
        speed1powerup.y = -20 # Hide from screen
        s1enabled = True # Activate powerup - Speed
        hiddens1l = False # Show timer of the Powerup
        pupvis1 = False # Powerup visible on screen

        # If you pickup a powerup while you have an anotherone add time to it
        if timeleft_s1 > 0:
            timeleft_s1 += poweruptime # Adding poweruptime to timeleft powerup
        else:
            timeleft_s1 = poweruptime # Resetting powerup timeleft
            thread_s1tl = threading.Thread(target=timeleft_s1tl,)
            thread_s1tl.start() # Start timer and more

# Player2
# Movement
def player2fncup():
    global player2speedup

    # Move player by
    player2.y += player2speedup
def player2fncdown():
    global player2speeddown

    # Move player by
    player2.y += player2speeddown
# Props
def player2prop():
    global poweruptime, hiddenw2l, hiddens2l, w2enabled, s2enabled, pupvis2, timeleft_w2, timeleft_s2
    
    #Preventing leaving from playspace
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= screenH:
        player2.bottom = screenH
        
    # Touching powerups
    # Wider powerup
    if player2.colliderect(powerup2wider):
        powerup2wider.y = -20 # Hide from screen
        player2.height = 200 # Activate powerup - Wide
        pupvis2 = False # Powerup visible on screen
        w2enabled = True # Activate Status
        hiddenw2l = False # Show timer of the Powerup

        # If you pickup a powerup while you have an anotherone add time to it
        if timeleft_w2 > 0:
            timeleft_w2 += poweruptime # Adding poweruptime to timeleft powerup
        else:
            timeleft_w2 = poweruptime # Resetting powerup timeleft
            thread_w2tl = threading.Thread(target=timeleft_w2tl,)
            thread_w2tl.start() # Start timer and more

    # Speed powerup
    if player2.colliderect(speed2powerup):
        speed2powerup.y = -20 # Hide from screen
        s2enabled = True # Activate powerup - Speed
        hiddens2l = False # Show timer of the Powerup
        pupvis2 = False # Powerup visible on screen

        # If you pickup a powerup while you have an anotherone add time to it
        if timeleft_s2 > 0:
            timeleft_s2 += poweruptime # Adding poweruptime to timeleft powerup
        else:
            timeleft_s2 = poweruptime # Resetting powerup timeleft
            thread_s2tl = threading.Thread(target=timeleft_s2tl,)
            thread_s2tl.start() # Start timer and more
            
# AutoBot
def player2BOT():
    global p2speedonBOT

    if waittime == 0: # Preventing move on countdown
        # Follow the ball
        if ball.y >= player2.y:
            player2.y += p2speedonBOT
        elif ball.y <= player2.y:
            player2.y -= p2speedonBOT

# Displays
def displays():
    # Scoreboards
    # P1
    statp1_text = ffam.render(f"{statp1}", False, lightgrey)
    screen.blit(statp1_text, (screenW/2+50, 20))
    # P2
    statp2_text = ffam.render(f"{statp2}", False, lightgrey)
    screen.blit(statp2_text, (screenW/2-55, screenH-50))
    
    # Wait display
    wait_text = ffam.render(f"{waittime}", False, lightgrey)
    if waittime > 0:
        screen.blit(wait_text, (screenW/2-50, screenH/2-19)) # Show
    else:
        screen.blit(wait_text, (screenW/2-50, -50)) # Hide

    # Powerups timeleft
    # Wide
    # P1
    w1_timeleft = ffam.render(f"{timeleft_w1}", False, orange) # Define timeleft counter
    if hiddenw1l == True:
        screen.blit(w1_timeleft, (screenW/2-100, screenH+50)) # Hide
    else:
        screen.blit(w1_timeleft, (screenW/2-100, screenH-50)) # Show
    # P2
    w2_timeleft = ffam.render(f"{timeleft_w2}", False, orange) # Define timeleft counter
    if hiddenw2l == True:
        screen.blit(w2_timeleft, (screenW/2+105, -50)) # Hide
    else:
        screen.blit(w2_timeleft, (screenW/2+105, 20)) # Show
        
    # Speed
    # P1
    s1_timeleft = ffam.render(f"{timeleft_s1}", False, aqua) # Define timeleft counter
    if hiddens1l == True:
        screen.blit(s1_timeleft, (screenW/2-150, screenH+50)) # Hide
    else:
        screen.blit(s1_timeleft, (screenW/2-150, screenH-50)) # Show
    # P2
    s2_timeleft = ffam.render(f"{timeleft_s2}", False, aqua) # Define timeleft counter
    if hiddens2l == True:
        screen.blit(s2_timeleft, (screenW/2+155, -50)) # Hide
    else:
        screen.blit(s2_timeleft, (screenW/2+155, 20)) # Show

while settingsdone == False: # Settings screen
    # Parsing values to string
    # Player count
    if p1mode == True:
        stateofplayermode = "1"
    elif p1mode == False:
        stateofplayermode = "2"
        
    # State of powerups
    if pupall == True:
        stateofpupsunblock = "Igen"
    elif pupall == False:
        stateofpupsunblock = "Nem"
        
    # State of bot's powerups
    if pupbot == True:
        stateofbotpups = "Igen"
    elif pupbot == False:
        stateofbotpups = "Nem"
    
    # Visual text's
    screen.fill(bgcolor)
    stateofplayermod = ffam.render(f"{stateofplayermode}" + " Játékos", False, lightgrey)
    stateofplayermod_desc = ffam.render(f"Egyszemélyes (Automate ellenfél) vagy kétszemélyes játék (1=P1 / 2=P2)", False, lightgrey)
    stateofbotpups = ffam.render(f"{stateofbotpups}", False, lightgrey)
    stateofbotpups_desc = ffam.render(f"Powerup engedélyezett BOT Számára (B=Igen / K=Nem)", False, lightgrey)
    
    stateofpupsunblock = ffam.render(f"{stateofpupsunblock}", False, lightgrey)
    stateofpupsunblock_desc = ffam.render(f"Powerup engedélyezett (A=Igen / N=Nem)", False, lightgrey)
    
    puptime = ffam.render(f"{poweruptime-1}" + "s", False, lightgrey)
    puptime_desc = ffam.render(f"Powerup hatásidőtartam (Bal nyíl - 1s, Jobb nyíil + 1s)", False, lightgrey)
    
    # Showing visual things in their order
    screen.blit(stateofplayermod_desc, (25, 20))
    screen.blit(stateofplayermod, (25, 50))
    
    if p1mode == True:
        screen.blit(stateofpupsunblock_desc, (25, 100))
        screen.blit(stateofpupsunblock, (25, 130))
        if pupall == True:
            screen.blit(stateofbotpups_desc, (25, 180))
            screen.blit(stateofbotpups, (25, 210))
            screen.blit(puptime_desc, (25, 260))
            screen.blit(puptime, (25, 290))
    elif p1mode == False:
        screen.blit(stateofpupsunblock_desc, (25, 100))
        screen.blit(stateofpupsunblock, (25, 130))
        if pupall == True:
            screen.blit(puptime_desc, (25, 180))
            screen.blit(puptime, (25, 210))
    
    startgame = ffam.render(f"Starthoz Enter", False, lightgrey)
    screen.blit(startgame, (25, screenH-50))        
        
    # Input handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            # ESC EXIT
            if event.key == pygame.K_ESCAPE:
                exit()
            # Settings done
            elif event.key == pygame.K_RETURN:
                settingsdone = True
            # Poweruptime set
            elif event.key == pygame.K_LEFT:
                if poweruptime > 2:
                    poweruptime -= 1
            elif event.key == pygame.K_RIGHT:
                if poweruptime < 99:
                    poweruptime += 1
            # Powerup allow or disable
            elif event.key == pygame.K_a:
                pupall = True
            elif event.key == pygame.K_n:
                pupall = False
            # PUP For Bots
            elif event.key == pygame.K_b:
                pupbot = True
            elif event.key == pygame.K_k:
                pupbot = False
            # P1 P2
            elif event.key == pygame.K_1:
                p1mode = True
            elif event.key == pygame.K_2:
                p1mode = False
    
    # Update screen
    pygame.display.flip()
    clock.tick(60)
    
# Ball Start Counter
thread_wait = threading.Thread(target=ballstart,)
thread_wait.start() # Starting countdown on thread

while True: # Main Game
    # Visual, displaying elements
    screen.fill(bgcolor)
    
    # Displaying visual things
    pygame.draw.rect(screen, white, ball)
    pygame.draw.rect(screen, white, player1)
    pygame.draw.rect(screen, white, player2)
    pygame.draw.aaline(screen, lightgrey, (screenW/2, 0), (screenW/2, screenH))
    pygame.draw.rect(screen, black, goal1)
    pygame.draw.rect(screen, black, goal2)
    pygame.draw.rect(screen, orange, powerup1wider)
    pygame.draw.rect(screen, aqua, speed1powerup)
    pygame.draw.rect(screen, orange, powerup2wider)
    pygame.draw.rect(screen, aqua, speed2powerup)

    # Motor
    displays()
    ballfnc()
    player1fncup()
    player1fncdown()
    player1prop()
    player2prop()

    # Check Player Mode
    if p1mode == False:
        player2fncup()
        player2fncdown()
    elif p1mode == True:
        player2BOT()
        
    if pupall == True:
        # Powerup, SpawnBlocker
        # P1
        if blocker1 == False:
            thread_pup1 = threading.Thread(target=spawncalc1,)
            thread_pup1.start()
        # P2
        if pupbot == True:
            if blocker2 == False:
                thread_pup2 = threading.Thread(target=spawncalc2,)
                thread_pup2.start()
        if p1mode == False:
            if blocker2 == False:
                thread_pup2 = threading.Thread(target=spawncalc2,)
                thread_pup2.start()
    
    # Input handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            # ESC EXIT
            if event.key == pygame.K_ESCAPE:
                exit()

            # P1
            if event.key == pygame.K_w:
                if s1enabled == True:
                    player1speedup = -8
                else:
                    player1speedup = -5
            if event.key == pygame.K_s:
                if s1enabled == True:
                    player1speeddown = 8
                else:
                    player1speeddown = 5
            # P2
            if p1mode == False:
                if event.key == pygame.K_UP:
                    player2speedup = -5
                if event.key == pygame.K_DOWN:
                    player2speeddown = 5 

        if event.type == pygame.KEYUP:
            # P1
            if event.key == pygame.K_w:
                player1speedup = 0
            if event.key == pygame.K_s:
                player1speeddown = 0
            # P2
            if p1mode == False:
                if event.key == pygame.K_UP:
                    player2speedup = 0
                if event.key == pygame.K_DOWN:
                    player2speeddown = 0
        
    # Update screen
    pygame.display.flip()
    clock.tick(60)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    