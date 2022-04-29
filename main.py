## MAIN FILE
# drawings of 4 screens, logical judgement

from cmu_112_graphics import *

import random, time, string
from bubble import Bubble, Player, Powerup
import back
import config

level = 0
#################################
# Splash Screen Mode
#################################
def splashScreenMode_mousePressed(app,event):
    
    # type username
    if event.x >= app.width/2 -20 and event.x <= app.width/2 +160 and event.y >= app.height/2 -60 and event.y <= app.height/2 -10:
        app.typingName = True
    else:
        app.typingName = False
    # type password
    if event.x >= app.width/2 -20 and event.x <= app.width/2 +160 and event.y >= app.height/2 +20 and event.y <= app.height/2 +70: 
        app.typingPassword = True
    else:
        app.typingPassword = False
    
    # click register
    if (event.x >=app.width/3+200 and event.y >=app.height/2 +110 and
        event.x<= app.width/3+310 and event.y<=app.height/2 +180):
        userBase = back.getUserDict()
        username = back.listToString(app.name)
        password = back.listToString(app.password)
        if username in userBase:
            app.splashpageMessage = 'This account already exists. \n Please log in'
        else:
            # editing file from: https://thispointer.com/how-to-append-text-or-lines-to-a-file-in-python/
            with open('user.txt','a') as file_object:
                file_object.write(username + '\n' + password + "\n" + '0\n' + '0,0,0,0' +'\n' )
            app.splashpageMessage = 'Registered! \n Enter your username and password to login'
    
    # click login
    if (event.x >=app.width/3-20 and event.y >=app.height/2 +110 and
        event.x<= app.width/3+90 and event.y<=app.height/2 +180):
        userBase = back.getUserDict()
        username = back.listToString(app.name)
        password = back.listToString(app.password)
        # check if the username exists
        if username in userBase:
            # check if the password is correct
            if userBase[username][0] == password:
                # enter the main page
                app.mode = 'mainMode'
                app.user =username
            else:
                app.splashpageMessage = 'Incorrect Password..'
        else:
            app.splashpageMessage = 'Please register the account first'

                      
def splashScreenMode_keyPressed(app,event):
    if app.typingName:
        if len(app.name) >= 11:
            app.splashpageMessage = '11 characters max for username'
            if event.key =='Backspace' or event.key =='Delete' :
                app.name.pop()
                if len(app.name) <= 11:
                    app.splashpageMessage = ''
            
        else:
            L = ["Tab", 'Enter', 'Escape', 'Left','Right','Up', 'Down','Space']
            if event.key in L:
                app.splashpageMessage = f"{event.key} couldn't appear in your username"
                
            elif event.key == 'Backspace' or event.key =='Delete' :
                if  len(app.name) >0 :
                    app.splashpageMessage = ''
                    app.name.pop()
            else:
                app.splashpageMessage = ''
                app.name.append(event.key)
        
    if app.typingPassword:
        if len(app.password) >= 11:
            app.splashpageMessage = '11 characters max for password'
            if event.key =='Backspace' or event.key =='Delete' :
                app.password.pop()
                if len(app.password) <= 11:
                    app.splashpageMessage = ''
        else:

            L = ["Tab", 'Enter', 'Escape', 'Left','Right','Up', 'Down','Space']
            if event.key in L:
                app.splashpageMessage = f"{event.key} couldn't appear in your username"
                
            elif event.key == 'Backspace' or event.key =='Delete':
                if  len(app.password) >0 :
                    app.splashpageMessage = ''
                    app.password.pop()
            else:
                app.splashpageMessage = ''
                app.password.append(event.key)

def splashScreenMode_timerFired(app):
    if time.time()-app.time0 >=0.6:
        app.title1 = not app.title1
        app.time0 = time.time()

def splashScreenMode_redrawAll(app,canvas): 
    canvas.create_image(400, 400, image = ImageTk.PhotoImage(app.background))
    # title
    if app.title1:
        for i in range(3):
            L = ['Type','and' ,'Learn']
            color = ['coral4','black','coral4']
            canvas.create_text(300+100*i,100+80*i, text = L[i], font = 'Broadway 30 bold', fill = color[i])
    else:
        for i in range(3):
            L = ['Type','and' ,'Learn']
            color = ['coral4','black','coral4']
            canvas.create_text(320+100*i,90+80*i, text = L[i], font = 'Broadway 30 bold', fill = color[i])

    # display message 
    canvas.create_text(app.width/2, app.height*0.85,
                        text = app.splashpageMessage, font = 'Comic\ Sans\ MS 24 bold')
    # username
    canvas.create_text( app.width/3-10, app.height/2-40,   
                        text = 'Username:', font = 'Comic\ Sans\ MS 24 bold')
    canvas.create_rectangle( app.width/2-20, app.height/2 -60,
                            app.width/2+160, app.height/2-10,
                            outline = 'black')

    # type username 
    username = back.listToString(app.name)
    canvas.create_text (app.width/2-5, app.height/2-35, 
                        text = username, anchor = 'w', 
                        font = 'Comic\ Sans\ MS 20 bold')
    # password 
    canvas.create_text( app.width/3-10, app.height/2+40,   
                        text = 'Password:', font = 'Comic\ Sans\ MS 24 bold')

    canvas.create_rectangle( app.width/2-20, app.height/2 +20,
                            app.width/2+160, app.height/2+70,
                            outline = 'black')
    # type password 
    password = back.listToString(app.password)
    canvas.create_text (app.width/2-5, app.height/2+45, 
                        text = password, anchor = 'w', 
                        font = 'Comic\ Sans\ MS 20 bold')
    # login & register button
    canvas.create_rectangle (   app.width/3-20, app.height/2 +110,
                                app.width/3+90, app.height/2 +180,
                                outline = 'black')                   
    canvas.create_text(app.width/3+35, app.height/2 +145,
                         text = 'Log In', font = 'Comic\ Sans\ MS 18')
    canvas.create_rectangle (   app.width/3+200, app.height/2 +110,
                                app.width/3+310, app.height/2 +180,
                                outline = 'black')                   
    canvas.create_text(app.width/3+255, app.height/2 +145,
                         text = 'Register', font = 'Comic\ Sans\ MS 18')
##################################################
 # main page
##################################################
# some code related to sidescroller from: https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#sidescrollerExamples
def makePlayerVisible(app):
    # scroll to make player visible as needed
    if (app.playerX < app.scrollX + app.scrollMargin):
        app.scrollX = app.playerX - app.scrollMargin
    if (app.playerX > app.scrollX + app.mapWidth - app.scrollMargin):
        app.scrollX = app.playerX - app.mapWidth + app.scrollMargin

def movePlayer(app, dx, dy):
    app.playerX += dx
    app.playerY += dy
    makePlayerVisible(app)
    overLap(app)

def overLap(app) :
    image = [app.castle1, app.castle2, app.castle3, app.castle4]
    for i in range(4):
        if abs(app.playerX - app.map[i][0]) <= image[i].width/2 + 20 and abs(app.playerY - app.map[i][1]) <= image[i].height + 20:
            if i <= int(back.getUserHighestLevel(app.user)) :
                return i
    return None
def drawmap(app,canvas):
    mapColor = []
    for i in range(4):
        if i <= int(back.getUserHighestLevel(app.user)) :
            mapColor.append('indian red')
        else :
            mapColor.append('gold3')
    # draw the dots, shifted by the scrollX offset
    for i in range(len(app.map)):
        image = [app.castle1, app.castle2, app.castle3, app.castle4]
        (cx,cy) = app.map[i]
        r = 40
        cx -= app.scrollX  # <-- This is where we scroll each dot!!!
        canvas.create_image(cx, cy, image =ImageTk.PhotoImage(image[i]) )
        canvas.create_line(cx-image[i].width/2-5, cy+image[i].height/2+10, cx+image[i].width/2-5, cy+image[i].height/2+10, width =4, fill = mapColor[i])
        canvas.create_text(cx,cy+image[i].height/2+20, text = f'{i+1}', font = 'Broadway 12 bold')
    canvas.create_line(0,250,app.width,250,dash = (4,1), width =4, fill = 'SteelBlue4')
    canvas.create_line(0,650,app.width,650,dash = (4,1), width =4, fill = 'SteelBlue4')

def mainMode_redrawAll(app,canvas):
    canvas.create_image(200, 400, image = ImageTk.PhotoImage(app.background2))
    canvas.create_text(80, 200, text = 'Explore your journey', font = 'Castellar 24 bold', anchor = 'w')

    
    drawmap(app,canvas)
    canvas.create_rectangle(0.85*app.width-20, 0.85*app.height-20, 0.85*app.width+120,0.85*app.height+90, fill = 'misty rose', width = 0)
    canvas.create_text(0.85*app.width+50, 0.85*app.height+35, font = 'Ink\ Free 18', text = 'ScoreBoard')
    # user name & log out
    canvas.create_text( app.width*0.9, app.height * 0.1, 
                        text = f'User: {app.user}', font = 'Ink\ Free 20 bold')
    canvas.create_rectangle(app.width*0.85, app.height*0.02,app.width*0.95, app.height* 0.08,
                            fill = 'misty rose', width = 0)
    canvas.create_text(app.width*0.9, app.height* 0.05, text = 'Log Out', font = 'Ink\ Free 14')
    canvas.create_text(app.width*0.4, 700, text =app.mainmodeMessage, font = 'Ink\ Free 23 bold')
    # draw level castles
    cx, cy = app.playerX, app.playerY
    cx -= app.scrollX # <-- This is where we scroll the player!!!
    canvas.create_image(cx,cy, image = ImageTk.PhotoImage(app.location))


def mainMode_keyPressed(app,event):
    if (event.key == "Left"):    movePlayer(app, -10, 0)
    elif (event.key == "Right"): movePlayer(app, +10, 0)
    elif (event.key == "Up"): movePlayer(app, 0, -5)
    elif (event.key == "Down"): movePlayer(app, 0, +5)
    elif (event.key == 'Enter'): 
        if overLap(app)!= None: 
            app.mode = 'gameMode'
            global level
            level = overLap(app)
            restart(app,level)
        else:
            app.mainmodeMessage = 'Pass the previous levels to unlock'
            app.hintTime = time.time()
            app.hint = True
    elif (event.key == 'Space'):
        back.updateUserHighestLevel(app.user,str(4))


def mainMode_timerFired(app):
       if app.hint:

           if time.time() -app.hintTime >=1.5:
                app.mainmodeMessage = 'Move to the castle & press Enter to start...'
                app.hint = False

def mainMode_mousePressed(app,event):
    # click on logout
    if event.x >= app.width*0.85 and event.y >= app.height*0.02 and event.x <= app.width *0.95 and event.y<= app.height*0.08:
        app.mode = 'splashScreenMode'
        app.name = []
        app.password = []
        app.splashpageMessage = ''
        app.playerX = 200 #player's center
        app.playerY = 430
    # click the scoreboard
    if event.x >= 0.85*app.width-20 and event.y >=0.85*app.height-20 and event.x <= 0.85*app.width+120 and event.y <= 0.85*app.height+90:
        app.mode = 'scoreMode'  

###############################################################
## ScoreBoard
###############################################################
def scoreMode_mousePressed(app,event):
    if event.x >= 657 and event.y >= 664 and event.x <= 743 and event.y <= 736:
        app.mode = 'mainMode'

def drawNames(app,canvas):
    origSort = back.getSortedNames()
    # only display the top seven users
    if len(origSort) >= 7:
        sortedName = origSort[:7]
    else:
        sortedName = origSort
    for i in range(len(sortedName)):
        canvas.create_text(app.width*0.26, 80*i+220, text = f'{sortedName[i]}', font= ' Comic\ Sans\ MS 20 ')

    scores = back.getAllUserScoreList(sortedName)
    for i in range(len(scores)):
        canvas.create_text(app.width*0.5, 80*i+220, text = f'{scores[i]}',font= ' Comic\ Sans\ MS 20 ')

    levels = back.getLevelList(sortedName)
    for i in range(len(levels)):
        canvas.create_text(app.width*0.75,80*i+220, text = f'{levels[i]}',font= ' Comic\ Sans\ MS 20 ' )

    


def scoreMode_redrawAll(app,canvas):
    canvas.create_image(400,400, image=ImageTk.PhotoImage(app.scoreImage))
    canvas.create_text(app.width*0.5, 30, text = 'ScoreBoard', font = 'Broadway 30 bold')
    title = ['Name', 'Score','Level']
    for i  in range(len(title)):
        canvas.create_text(app.width*0.25+i*200, 150, text = title[i], font = 'Castellar 21 bold')
    canvas.create_image(700,700, image = ImageTk.PhotoImage(app.returnButton))
    drawNames(app,canvas)

    
###############################################################################
def appStarted(app):
    app.title1 = False
    app.splashpageMessage = ''
    app.name = []
    app.password = []
    app.user ='' # assigned in the main page

    app.scrollX = 0
    app.radius = 40
    app.mapHeight = 300
    app.mapWidth = 500
    app.scrollMargin = 50
    app.map = [(0.6*app.mapWidth+100,0.78*app.mapHeight+250),(1.1*app.mapWidth+100, 0.47*app.mapHeight+250),
                (1.6*app.mapWidth+100,0.78*app.mapHeight+250),(2.2*app.mapWidth+100, 0.59*app.mapHeight+250)]

    app.playerX = 200 #player's center
    app.playerY = 430
    app.mainmodeMessage = 'Move to the castle & press Enter to start...'
    app.hintTime = time.time()
    app.hint = False

    app.typingName = False
    app.typingPassword = False
    app.mode = 'splashScreenMode'
    app.r = 40
    app.bubbles = [ ]

    app.typed = []
                            
    app.time0 = time.time()
    app.message = ''
    app.key = ''
    app.keytime = time.time()
    app.timerDelay = 20

    app.player = Player(config.initScore, config.life)

    app.gameOver = False
    app.qualifyScore = [5,7,9,11]
    app.qualifyMessage = ''

    app.timeRemaining = [20,20,20,30][level]
    app.timeUp = False
    app.gameDone = False
    app.nextLevel = False

    app.powerup = []
    app.power = False
    app.woho = False

    # load image from: https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#loadImageUsingFile
    app.image = None
    # image1 from: https://thebloomingjournal.com/marble-and-rose-gold-geometric-phone-wallpapers/
    app.image1 = app.loadImage('image/background.jpg')
    app.background = app.scaleImage(app.image1, 1.5)
    #image2 from: 
    app.image2 = app.loadImage('image/background2.jpg')
    app.background2 = app.scaleImage(app.image2,0.7)
    # restart icon from: https://www.flaticon.com/premium-icon/restart_2499151 
    app.image3 = app.loadImage('image/restartIcon.png')
    app.restartIcon = app.scaleImage(app.image3, 1/15)
    # arrow image from: https://www.iconfinder.com/icons/1013763/next_next_level_play_next_arrow_arrows_direction_forward_move_right_icon
    app.image4 = app.loadImage('image/nextLevel.png')
    app.nextLevelIcon = app.scaleImage(app.image4, 0.13)
    # image5 from: https://www.pinterest.com/pin/794392821754706509/
    app.image5 = app.loadImage('image/score.jpg')
    app.scoreImage = app.scaleImage(app.image5, 0.7)
    # image6 from: https://www.kindpng.com/imgv/hTRRhhx_return-button-return-button-image-png-transparent-png/
    app.image6 = app.loadImage('image/return.png')
    app.returnButton = app.scaleImage(app.image6, 0.08)
    #image7 from: https://www.vhv.rs/viewpic/iRoTw_circle-location-icon-png-transparent-png/
    app.image7 = app.loadImage('image/location.png')
    app.location = app.scaleImage(app.image7, 0.05)
    # castle images from: https://www.dreamstime.com/castle-cartoon-linear-drawing-coloring-outline-contour-simple-sketch-black-white-vector-illustration-drawn-palace-t-three-image122205742
    # https://line.17qq.com/articles/ijdgepibz.html
    app.image8 = app.loadImage('image/castle1.png')
    app.castle1 = app.scaleImage(app.image8, 0.3)
    app.image9 = app.loadImage('image/castle2.jpg')
    app.castle2 = app.scaleImage(app.image9, 0.2)
    app.image10 = app.loadImage('image/castle3.png')
    app.castle3 = app.scaleImage(app.image10, 0.25)
    app.image11 = app.loadImage('image/castle4.jpg')
    app.castle4 = app.scaleImage(app.image11, 0.16)
    # https://kids.nationalgeographic.com/science/article/the-truth-about-your-heart
    app.image12 = app.loadImage('image/heart.png')
    app.heart = app.scaleImage(app.image12, 0.05)


def restart(app,level):
    app.bubbles = [ Bubble( random.randint(app.r,520),app.r, 
                                    0, level*3+10, level )]

    app.typed = []
                            
    app.time0 = time.time()
    app.message = ''
    app.key = ''
    app.keytime = time.time()
    app.timerDelay = 20

    app.player = Player(config.initScore, config.life)

    app.gameOver = False
    app.qualifyScore = [5,7,8,10]
    app.qualifyMessage = ''

    app.timeRemaining = [15,20,25,40][level]
    app.timeUp = False
    app.gameDone = False
    app.nextLevel = False

    app.powerup = []
    app.power = False
    app.woho = False
################################################
#               Game Mode 
################################################
    
def gameMode_timerFired(app):
    if app.gameOver :
        return
    if app.timeUp: 
        return 

    else:
        if time.time() - app.keytime >= 0.25 :
            app.key = ''
        app.timeRemaining -= app.timerDelay/1000
        ## first check if GAMEOVER/ TIMEUP
        if app.player.life == 0:
            app.gameOver = True
            if back.checkLevelUp (app.player.score, app.qualifyScore, level):
                if level == 3:
                    app.gameDone = True
                    app.qualifyMessage = "You've passed all levels! \n Enjoy typing!"
                
                else:
                    app.nextLevel = True
                    app.qualifyMessage = f'CONG! You pass level {level+1}'

                # check and change the highest level of that player in the txt file
                highestLevel = back.getUserHighestLevel(app.user)
                if level +1 > int(highestLevel):
                    back.updateUserHighestLevel(app.user,str(level+1))

            else:
                app.qualifyMessage = 'Oops. Try again'
            # update the level score
            scorelist = back.getScoreList(app.user)
            highestScore = scorelist[level]
            if app.player.score >int(highestScore):
                back.updateHighestScore(app.user,level, app.player.score)

        if app.timeRemaining <= 0 :
            app.timeUp =  True
            if back.checkLevelUp (app.player.score, app.qualifyScore, level):
                if level == 3:
                    app.gameDone = True
                    app.qualifyMessage = "You've passed all levels! \n Enjoy typing!"
                
                else:
                    app.nextLevel = True
                    app.qualifyMessage = f'CONG! You pass level {level+1}'
                # check and change the highest level of that player in the txt file
                highestLevel = back.getUserHighestLevel(app.user)
                if level +1 > int(highestLevel):
                    back.updateUserHighestLevel(app.user,str(level+1))
            else: 
                app.qualifyMessage = 'Oops. Try again'
            # update the level score
            scorelist = back.getScoreList(app.user)
            highestScore = scorelist[level]
            if app.player.score >int(highestScore):
                back.updateHighestScore(app.user,level, app.player.score)


        ###### COLLISION CHECK ########
        for i in range(len(app.bubbles)):
            for j in range(len(app.bubbles)):
                if i < j:
                    if app.bubbles[i].isCollide(app.bubbles[j]):
                        # dosteps
                        v1 = app.bubbles[i].collide(app.bubbles[j])
                        v2 = app.bubbles[j].collide(app.bubbles[i])
                        app.bubbles[i].xspeed, app.bubbles[i].yspeed = v1[0], v1[1]
                        app.bubbles[j].xspeed, app.bubbles[j].yspeed = v2[0], v2[1]

        ## check if powerup intersect with other bubbles -> disappear
        for powerup in app.powerup:
            for bubble in app.bubbles:
                if powerup.checkOverlap(bubble):
                    app.powerup.remove(powerup)
                    break

        # bubble movement
        for bubble in app.bubbles:
            cx = bubble.coordinate[0]
            cy = bubble.coordinate[1]
            # when bubble reaches the bottom
            if cy+40 >= app.height:
                bubble.bottomCount +=1
                # bounce the ball first time hitting the ground
                if bubble.bottomCount ==1:
                    bubble.bounce()
                # the second time-> disappear
                else:
                    app.bubbles.remove(bubble)
                    app.player.life -=1

            # bounce within the screen:
            if cx-app.r< 0 or cx+app.r >= app.width*0.7:
                bubble.xspeed = -bubble.xspeed
            
            if cy-app.r < 0:
                bubble.yspeed = -bubble.yspeed
            bubble.moveBubble()


        if app.woho:
            app.power = True
            for powerup in app.powerup:
                if powerup.coordinate[1] + app.r >= app.height:
                    app.powerup.remove(powerup)
                # if powerup
                powerup.moveBubble()
            if len(app.powerup) == 0:
                app.power = False
                app.woho = False
        timeInterval = [4,2,2,1.5]      
        # after 3 seconds, get a new bubble
        if time.time() -app.time0 >= timeInterval[level]:
            if level == 3:
                if random.randint(0,2) == 1 :
                    newBubble = Bubble(random.randint(app.r,520),random.randint(app.r,200), 
                                    level*3+9, 0, level )
                else :
                    newBubble = Bubble(random.randint(app.r,100),random.randint(app.r,200), 
                                    0,level*3+9, level)

            else :
                newBubble = Bubble( random.randint(app.r,520),app.r, 
                                    0, level*3+8, level )
            
            # if they typed wrong a letter, drop based on that
            if app.player.getwrongTotal() >=1:
                wrongPercentage = app.player.wrongPercentage()
                wrongLetters = app.player.getWrongLetters()
                
                
                newBubble.word = newBubble.setWord(wrongPercentage)
                newBubble.wordColor = ['black'] *len(newBubble.word)
            app.bubbles.append(newBubble)
            app.time0 = time.time()


def gameMode_keyPressed(app,event):
    if app.gameOver:
        return 
    if app.timeUp:
        return
    else:
        L = ['Space', 'Tab','Delete', 'Escape', 'Enter']
        if event.key not in string.ascii_letters:
        # if event.key in string.punctuation or event.key in string.digits or event.key in L:
            app.message = 'Key invalid'
        else:
        ################# EDIT WORD COLOR ######################
            app.message = ''
            app.typed.append(event.key.lower())
            removed = False
            app.player.allTyped[event.key.lower()] += 1
            if len(app.typed) == 1:
                flag = False
                # check if that's the beginning of some word
                for bubble in app.bubbles:
                    if app.typed[0] == bubble.word[0]:
                        # turn the first letter into red
                        bubble.wordColor[0] = 'red'
                        flag = True
                        if len(bubble.word) == 1:
                            app.bubbles.remove(bubble)
                            app.player.score += 1
                            app.player.words.append(bubble.word)
                            app.typed = []
                            app.key = bubble.word
                            app.keytime = time.time()
                            removed = True
                            break
                    
                if not flag:
                    # after the loop, key does not fit
                    # remove the key
                    app.typed.remove(event.key.lower())

            else:
                flg = False
                for bubble in app.bubbles:
                    innerflg = True
                    if len(app.typed) == 0 :
                        bubble.wordColor = ['black'] * len(bubble.word)
                    for i in range(len(app.typed)):
                        if len(bubble.word) < len(app.typed):
                            innerflg = False
                            break
                        if bubble.word[i] != app.typed[i]:
                            # set that word to black
                            innerflg = False
                            if bubble.wordColor[i-1] =='red':
                                bubble.wordColor = ['black'] * len(bubble.word)
                                app.player.wrong[bubble.word[i]]+=1

                            break
                        else:
                            bubble.wordColor[i] = 'red'
                    if innerflg:
                        flg = True
                        if len(bubble.word) == len(app.typed):
                            app.bubbles.remove(bubble)
                            app.player.score += 1
                            app.player.words.append(bubble.word)
                            app.typed = []
                            app.key = bubble.word
                            app.keytime = time.time()
                            removed = True
                        
                if not flg:
                    app.typed = []
            if len(app.typed) == 0 :
                for bubble in app.bubbles:
                    bubble.wordColor = ['black'] * len(bubble.word)
            if not removed :
                app.key = back.listToString(app.typed)
                app.keytime = time.time()

            response= app.player.setStatus()
            if response:  ## enter powerup status

                app.woho = True
                if app.player.status == 'good':
                    p = random.randint(1,100)
                    if p <=10:
                        new = Powerup(random.randint(app.r,520),app.r*0.5, 0, 
                                            level*5+10, level)
                        attr = new.setAttr(app.player.status)
                        if len(app.powerup) >=3:
                            app.powerup.pop(0)
                            app.powerup.append(new)
                        else:
                            app.powerup.append(new)
                else:
                    p = random.randint(1,100)
                    if p <=10:
                        new = Powerup(random.randint(app.r,520),app.r*0.5, 0, 
                                            level*5+10, level)
                        attr = new.setAttr(app.player.status)
                        if len(app.powerup) >=3:
                            app.powerup.pop(0)
                            app.powerup.append(new)
                        else:
                            app.powerup.append(new)

def gameMode_mousePressed(app,event):
    if app.power:
        for powerup in app.powerup:
            cx = powerup.coordinate[0]
            cy = powerup.coordinate[1]
            r = app.r 
            if back.isInCircle(cx ,cy, r, event.x, event.y):
                # give different attribute for different powerup status
                if powerup.attr == 'speedup':
                    for bubble in app.bubbles:
                        bubble.yspeed += 5
                if powerup.attr =='slowdown':
                    for bubble in app.bubbles:
                        bubble.yspeed -= 2
                if powerup.attr == 'addscore':
                    app.player.score += 1
                if powerup.attr =='minusscore':
                    app.player.score -= 1
                app.powerup.remove(powerup)


    # restart the game
    if app.gameOver or app.timeUp:
        if (event.x >= 706 and 
        event.x <= 774 and 
        event.y >= 716 and 
        event.x <= 784 ):
            # proceed to the next level
            if app.nextLevel:
                ## global learned from: https://www.programiz.com/python-programming/global-keyword
                global level 
                level += 1
                restart(app,level)
            else:
                restart(app,level)
    # back to main mode 
    if event.x >= 607 and event.y >= 714 and event.x <= 693 and event.y <= 786:
        app.mode = 'mainMode'
###################################################
#                    Draw
####################################################
def drawBubbles(app,canvas):
    for bubble in app.bubbles:
        bubbleX = bubble.coordinate[0]
        bubbleY = bubble.coordinate[1]
        canvas.create_oval( bubbleX-app.r, bubbleY-app.r,
                            bubbleX +app.r,bubbleY +app.r,
                            fill = 'light blue', outline = 'white')
        # draw individual letter
        if len(bubble.word) %2 ==0:
            for i in range(len(bubble.word)):
                canvas.create_text( bubbleX-11*len(bubble.word)//2+11*i+5, 
                                    bubbleY, 
                                    text = bubble.word[i], font = 'Comic\ Sans\ MS 13 ',
                                    fill = bubble.wordColor[i])
        else:
            for i in range(len(bubble.word)):
                canvas.create_text( bubbleX-10*len(bubble.word)//2+10*i+7, 
                                    bubbleY,    
                                    text = bubble.word[i], font = 'Comic\ Sans\ MS 13',
                                    fill = bubble.wordColor[i])
def drawPowerup(app,canvas):
    if app.power:
        for powerup in app.powerup:
            cx = powerup.coordinate[0]     
            cy = powerup.coordinate[1]   
            r = app.r*0.5
            canvas.create_oval(cx-r, cy-r, cx+r, cy+r,
                                fill = 'red')

def drawSideBars(app,canvas):
    canvas.create_line( 0.7*app.width,0, 
                        0.7*app.width, app.height)
    canvas.create_text( 0.85*app.width, 60, text = f'Score = {app.player.score}',
                        font = 'Comic\ Sans\ MS 15')
    canvas.create_text(0.85*app.width, 280, text = 'Current Typing...',
                        font = 'Comic\ Sans\ MS 20')
    canvas.create_text( 0.85*app.width, 360, text = app.key,
                        font = 'Comic\ Sans\ MS 40')
    canvas.create_text( 0.85*app.width, 120, 
                        text = f'time = {back.roundHalfUp(app.timeRemaining)}',
                        font = 'Comic\ Sans\ MS 15')
    # draw lives
    for i in range(app.player.life):
        canvas.create_image(0.74*app.width+i*45, 170, image =ImageTk.PhotoImage(app.heart))

    canvas.create_text( 0.85*app.width, 360,text = app.message,
                        font = 'Comic\ Sans\ MS 16')
    canvas.create_text( 0.85*app.width, 610, text = f'You are at level {level+1}',
                        font = 'Comic\ Sans\ MS 16')
   
    
def drawState(app,canvas):
    if app.gameOver:
        canvas.create_oval(0.1*app.width, 0.35*app.height,
                                0.6*app.width, 0.65*app.height,
                                fill = 'lemon chiffon', width =0)
        canvas.create_text( 0.35*app.width, 0.45*app.height, 
                            text = 'Game Over!',
                            font = 'Comic\ Sans\ MS 16')
        canvas.create_text( 0.35*app.width, 0.55*app.height, 
                            text = f'{app.qualifyMessage}',
                            font = 'Comic\ Sans\ MS 16')
        if app.nextLevel:
            canvas.create_image(740,750, 
                            image=ImageTk.PhotoImage(app.nextLevelIcon))
        if app.nextLevel== False and app.gameDone == False:
            canvas.create_image(740,750, 
                                image=ImageTk.PhotoImage(app.restartIcon))

    if app.timeUp:
        canvas.create_oval(0.1*app.width, 0.35*app.height,
                                0.6*app.width, 0.65*app.height,
                            fill = 'lemon chiffon', width =0)        
        canvas.create_text( 0.35*app.width, 0.45*app.height, 
                            text = 'Time is UP!',
                            font = 'Comic\ Sans\ MS 16')
        canvas.create_text( 0.35*app.width, 0.55*app.height, 
                            text = f'{app.qualifyMessage}',
                            font = 'Comic\ Sans\ MS 16')
        if app.nextLevel:
            canvas.create_image(740, 750, 
                            image=ImageTk.PhotoImage(app.nextLevelIcon))
        if app.nextLevel== False and app.gameDone == False:
            canvas.create_image(740, 750, 
                                image=ImageTk.PhotoImage(app.restartIcon))

def gameMode_redrawAll(app,canvas):
    drawBubbles(app,canvas)
    drawSideBars(app,canvas)
    drawState(app,canvas)
    drawPowerup(app,canvas)
    canvas.create_image(650,750, image = ImageTk.PhotoImage(app.returnButton))

    
runApp(width =config.width, height = config.height)