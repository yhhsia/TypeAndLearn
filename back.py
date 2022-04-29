#### This file contains only functions(helper function)

# check if could head into next level
def checkLevelUp(score, L, level):
    if score >= L[level]:
        return True
    return False

# from :https://www.cs.cmu.edu/~112/notes/notes-variables-and-functions.html#RecommendedFunctions

def roundHalfUp(d):
    import decimal
    rounding = decimal.ROUND_HALF_UP
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

# get a list of words including 'letter'
def wordlistbyLetter(letter,L):
    result = []
    for word in L:
        if letter in word:
            result.append(word)
    return result

# add up all values for a dic
def add(d):
    result = 0
    for key in d:
        result += d[key]
    
    return result

def isInCircle(cx ,cy, r, x, y):
    if ((x-cx)**2 + (y-cy)**2)** 0.5 <=r:
        return True 
    else:
        return False 

def addList(l1, l2):
    result = []
    for i in l1:
        result.append(i)
    for j in l2:
        result.append(j)
    return result

def listToString(L):
    result = ''
    for letter in L:
        result += letter
    return result

# from: https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

###############################################################
# Operations with user info
###############################################################

# store each user's attribute in a dictionary
# -> username, password, highest level, highest score for each level
def getUserDict():       
    all = readFile('user.txt')
    lines= all.splitlines()
    num = len(lines)
    result = dict()
    for i in range(0,num, 4):
        username = lines[i]
        password = lines[i+1]
        highestLevel = lines[i+2]
        scores = lines[i+3].split(',')
        result [username] = [password, highestLevel, scores]
    return result

def getUserList():
    users = [each for each in getUserDict()]
    return users

def getLevelList(L):
    result = []
    for user in L:
        result.append(getUserDict()[user][1])
    return result

# determine which line user's info starts in txt
def getUserIndex(user):
    users = getUserList()
    # users = [each for each in back.getUserDict()] # a list containing all users' name
    index = users.index(user)
    return index

def getUserHighestLevel(user):
    index = getUserIndex(user)
    return getUserDict()[user][1]

# edit the user highest Level in the txt file (third line)
# https://www.kite.com/python/answers/how-to-edit-a-file-in-python
def updateUserHighestLevel(user, currLevel):
    index = getUserIndex(user)
    f = open('user.txt')
    lines = f.readlines()
    lines[index*4+2] = currLevel + '\n'
    f = open('user.txt','w')
    new = ''.join(lines)
    f.write(new)

# a list of all scores 
def getScoreList(user):
    index = getUserIndex(user)
    s = getUserDict()[user][2]
    L = []
    for i in range(len(s)):
        L.append(s[i])
    return L

def getScoreTotal(user):
    scores = getScoreList(user)
    result =0
    for score in scores:
        result += int(score)
    return result

def getAllUserScoreList(L):
    result = []
    for user in L:
        result.append(getScoreTotal(user))
    return result

def updateHighestScore(user,currLevel, currScore):
    index = getUserIndex(user)
    f = open('user.txt')
    lines = f.readlines()
    # update the score
    scoreList = getScoreList(user)
    scoreList [currLevel] = str(currScore)
    newScore = ''
    for i in range (len(scoreList)):
        if i == len(scoreList) -1:
            newScore += scoreList[i]
        else:
            newScore += scoreList[i] + ','

    lines[index*4+3] = newScore + '\n'
    f = open('user.txt','w')
    new = ''.join(lines)
    f.write(new)

def getUserandScorePair():
    result = dict()
    users =  getUserList()
    # print(f'users = {users}')
    scores = getAllUserScoreList(users)
    for i in range(len(users)):
        result[users[i]] = scores[i]
    return result

def getSortedNames():
    d = getUserandScorePair()
    users = getUserList()
    origScore = getAllUserScoreList(users)
    scores = sorted(origScore)
    result= []
    for score in reversed(scores):
        for key in d:
            if d[key]!= None and int(d[key]) == int(score):
                result.append(key)
                d[key] = None
                break

    return result 







