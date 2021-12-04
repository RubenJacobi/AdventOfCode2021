import re

def filereader(filename):
    for line in open(filename, "r"):
        yield line.rstrip()

def parseFile():
    inputNumbers = []
    bingoCards = []
    bingoCard = []
    for index, line in enumerate(filereader("input4a")):
        print(type(line))
        line = line
        if index == 0:
            inputNumbers = line.split(",")
            continue
        elif index == 1:
            continue
        if line == "":
            continue
        
        digits = re.findall("\d+", line)
        
        print(digits)
        print(line)
        bingoCardLine = {d:False for d in digits}
        bingoCard.append(bingoCardLine)
        if len(bingoCard) == 5:
            bingoCards.append(bingoCard)
            bingoCard = []
    print(bingoCards)
    return inputNumbers,bingoCards
            


def markNumbers(bingoCards,number):
    print(f"{bingoCards}")
    for card in bingoCards:
        
        for cardline in card:
           # print(f"{cardline}")
            if number in cardline:
                cardline[number] = True
                
    return bingoCards
                

def calculate_win(bingoCard):
    verticals = [[],[],[],[],[]]
    print(f"{verticals=}")
    
    #horizontal
    for index,line in enumerate(bingoCard):
      
        if  all(value == True for value in line.values()):
            
            return line
        for i,item in  enumerate(line):
            print(f"{line=}")
            verticals[i].append(item)
    
    
    print(f"{verticals=}")
    for vertical in verticals:
         if  all(value == True for value in line.values()):
            return vertical
    
    return None

def calculate_score(bingoCard):
    score = 0
    for line in bingoCard:
        for key,value in line.items():
            print(value)
            if value == False:
                score = score + int(key)
                
    return score
                
                


def start():
    inputNumbers,bingoCards = parseFile()
    print(f"{bingoCards=}")
    
    for number in inputNumbers:
        bingoCards = markNumbers(bingoCards,number)
        #print(bingoCards[0])
        for bingoCard in bingoCards:
            winningLine = calculate_win(bingoCard)
            if winningLine != None:
                return bingoCard, number
            print("No Winner")

if __name__ == "__main__":
    winner, number = start()
    score = calculate_score(winner)
    output = int(number) * score
    print(f"{winner=}")
    print(f"{score=}")
    print(f"{output=}")