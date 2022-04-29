### This file contains all classes and their methods
import random, string
import wordlist, config, back, math
# trig functions from: https://www.geeksforgeeks.org/mathematical-functions-in-python-set-3-trigonometric-and-angular-functions/

class Bubble(object):
    def __init__(self, initCordX, initCordY, xspeed, yspeed, level):
        self.xspeed = xspeed
        self.yspeed = yspeed
        # set initial coordinate for each bubble
        self.coordinate = [initCordX, initCordY]
        # get a random word from 
        levelSet = [1, 2, 3, 3]
        self.levelIndex = levelSet[level]
        self.word = random.choice(wordlist.wordByLevel[self.levelIndex])
        self.wordColor = ['black'] * len(self.word)
        self.bottomCount = 0 
        self.gravity = 0.05  # acceleration
        self.r = 40 

    def moveBubble(self):
        # acceleration idea from https://adamdempsey90.github.io/python/bouncing_ball/bouncing_ball.html
        self.yspeed += self.gravity
        
        self.coordinate[1] += self.yspeed/6
        self.coordinate[0] += self.xspeed/6
    
    def bounce(self):
        self.yspeed *= -1
    
    # the dictionary containing all words in current level
    def wordPercentage(self):
        result = dict()
        for word in wordlist.wordByLevel[self.levelIndex]:
            result[word] = 0
        return result

    # compute the wrong percentage for each word in the current level
    def wordWrongP (self, wrongPercentage):
        result = self.wordPercentage()
        for word in result:
            for letter in word:
                # get the wrong percentage for each letter
                result[word] += wrongPercentage[letter]
        return result
                
    
    def setWord(self, wrongPercentage):
        p = random.randint(1,100)
        new =''
        if p  > 90: 
            new = random.choice(wordlist.wordByLevel[self.levelIndex])
        else:
            # get a word based on the letter frequently typed wrong            
            totalp = back.add(self.wordWrongP(wrongPercentage))
            prob = random.random() *totalp
            wordList = self.wordWrongP(wrongPercentage)
            sumSoFar = 0
            for word in wordList:
                if wordList[word] + sumSoFar >= prob:
                    new = word
                    return new
                sumSoFar += wordList[word]
        return new

        
    def isCollide(self, other):
        if ((self.coordinate[0]-other.coordinate[0])**2 + (self.coordinate[1]-other.coordinate[1])**2)**0.5 <= self.r + other.r:
            return True
        return False
    
    # collision background from: https://en.wikipedia.org/wiki/Elastic_collision#Equations
    def collide(self, other):
        cx1 = self.coordinate[0]
        cy1 = self.coordinate[1]
        cx2 = other.coordinate[0]
        cy2 = other.coordinate[1]
        velocityVector = [self.xspeed, self.yspeed]

        if velocityVector [0] == 0:
            if velocityVector[1] > 0 :
                velocityAngle = -math.pi/2   
            elif velocityVector[1] < 0 :
                velocityAngle = math.pi/2
        elif velocityVector[1] == 0:
            if velocityVector[0] >0:
                velocityAngle =0
            elif velocityVector[0] < 0:
                velocityAngle = math.pi
        else:
            velocityAngle = math.atan(velocityVector[1]/velocityVector[0])

        directionVector = [cx1-cx2, cy1-cy2]
        dirMag = math.hypot(directionVector[0], directionVector[1])
        unitVector = [directionVector[0]/dirMag, directionVector[1]/dirMag]

        # impulse vector changes the velocity
        if directionVector [0] ==0:
            if directionVector[1] >0:
                impulseAngle = math.pi/2
            else:
                impulseAngle = - math.pi/2
        else:
            impulseAngle = math.atan(directionVector[1]/directionVector[0])
        impulse_velocityAngle = impulseAngle - velocityAngle
        impulseMag = 2*abs(math.cos(impulse_velocityAngle))* math.hypot(velocityVector[0], velocityVector[1])
        impulseVector= [impulseMag*unitVector[0], impulseMag*unitVector[1]]
    
        fVector = [impulseVector[0]+velocityVector[0], impulseVector[1]+velocityVector[1]]
        finalVector_x = fVector[0] * math.hypot(velocityVector[0], velocityVector[1])/ math.hypot(fVector[0],fVector[1])
        finalVector_y = fVector[1] * math.hypot(velocityVector[0], velocityVector[1])/ math.hypot(fVector[0],fVector[1])
        
        finalVector = [finalVector_x, finalVector_y]
        return (finalVector)

class Player(object):
    def __init__(self,score, life):
        self.score = score
        self.life = life
        self.status = None

        self.allTyped = config.alphabets
        self.words = [] # all correctly typed words
        self.wrong = config.alphabets1
    
    def getwrongTotal(self):
        count = 0 
        for key in self.wrong:
            count += self.wrong[key]
        return count 

    def wrongPercentage(self):
        # map each letter in percentage -> how often they type the letter wrong
        result = dict.fromkeys(string.ascii_lowercase, 0)
        for key in result:
            result[key] = self.wrong[key] /self.getwrongTotal()
        return result
    
    def getWrongLetters(self):
        L = []
        for letter in self.wrong:
            if self.wrong[letter] >0:
                L.append(letter)
        return L


    def setStatus(self):
        wrong = self.getwrongTotal()
        total = back.add(self.allTyped)
        correct = total-wrong
        # return True if enter powerup status
        if correct/total >=0.8 and self.score >=2:
            self.status = 'good'
            return True
        elif wrong/total >= 0.25:
            self.status = 'bad'
            return True
        else:
            self.status = None 
            return False


class Powerup(Bubble):
    def __init__(self,initCordX,initCordY,xspeed, yspeed,level):
        super().__init__(initCordX,initCordY,xspeed, yspeed,level)
        self.attr = ''  


    # assign different attr based on user status 
    def setAttr(self, status):
        if status =='good':
            p = random.randint(1,100)
            if p <= config.pSpeedup:
                self.attr = 'speedup'
            else:
                self.attr = 'addscore'
        elif status =='bad':
            p = random.randint(1,100)
            if p < config.pSlowdown:
                self.attr = 'slowdown'
            else:
                self.attr = 'minusscore'
                
    # check if powerup intersects with other bubbles
    def checkOverlap(self, other):
        cx1 = self.coordinate[0]
        cy1 = self.coordinate[1]
        cx2 = other.coordinate[0]
        cy2 = other.coordinate[1]
        if math.hypot(cx1-cx2, cy1-cy2) <= 60:
            return True
        return False

    







                    

        



    

