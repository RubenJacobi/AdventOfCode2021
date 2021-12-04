import re

def filereader(filename):
    for line in open(filename, "r"):
        yield line.rstrip()

def parseFile():
    inputNumbers = []
    bingoCards = []
    bingoCard = []
    for index, line in enumerate(filereader("input4a")):
        
        line = line
        if index == 0:
            inputNumbers = line.split(",")
            continue
        elif index == 1:
            continue
        if line == "":
            continue
        
        digits = re.findall("\d+", line)
        
        bingoCardLine = {d:False for d in digits}
        bingoCard.append(bingoCardLine)
        if len(bingoCard) == 5:
            bingoCards.append(bingoCard)
            bingoCard = []
    
    return inputNumbers,bingoCards
            


def markNumbers(bingoCards,number):
    
    for card in bingoCards:
        
        for cardline in card:
            if number in cardline:
                cardline[number] = True
                
    return bingoCards
                

def calculate_win(bingoCard):
    verticals = [{},{},{},{},{}]
    
    for index,line in enumerate(bingoCard):
        if  all(value == True for value in line.values()):
            return True
        for i,item in  enumerate(line):
            verticals[i][item] = line[item]
            
    
    
    for vertical in verticals:
        
        if  all(value == True for value in vertical.values()):
            return True
    
    return False

def calculate_score(bingoCard):
    score = 0
    for line in bingoCard:
        for key,value in line.items():
            if value == False:
                score = score + int(key)
                
    return score
                
                


def start():
    inputNumbers,bingoCards = parseFile()
    lastNumber = 0
    lastBingoCard = {}
    while len(bingoCards) != 0:
        
        
        try:
            for index, number in enumerate(inputNumbers):
                lastNumber = int(number)

                bingoCards = markNumbers(bingoCards,number)
                #print(bingoCards[0])
                for bingoCard in bingoCards:
                    if calculate_win(bingoCard):
                        lastBingoCard = bingoCards[0]
                        bingoCards.remove(bingoCard)
                        raise Exception("new round")
        except Exception as e:
            pass
    
    return lastBingoCard, lastNumber
    
    

if __name__ == "__main__":
    winner, number = start()
    score = calculate_score(winner)
    output = int(number) * score
    
    print(f"{number=}")
    print(f"{score=}")
    print(f"{output=}")
    print(f"{winner=}")