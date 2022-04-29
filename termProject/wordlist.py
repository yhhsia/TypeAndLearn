## This file create classify different words from the txt file

# from https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
def readFile(path):
    with open(path, "rt") as f:
        return f.read()
        
# words file from https://gist.github.com/deekayen/4148741#file-1-1000-txt
allWords = readFile('basic1000 words.txt')
wordList = allWords.splitlines()
# store words in different levels in dict
wordByLevel = {
    1: list(),
    2: list(),
    3: list()
}
for word in wordList:
    if len(word) <=3:
        wordByLevel[1].append(word)
    elif 4<= len(word) <=5 :
        wordByLevel[2].append(word) 
    else:
        wordByLevel[3].append(word)
