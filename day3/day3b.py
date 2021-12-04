inputsize = -1

def filereader(filename):
    for line in open(filename, "r"):
        yield line.rstrip()


#
def getGamma():
    gamma = None
    for index, line in enumerate(filereader("day3binput")):
        if gamma == None:
            gamma= [0] * len(line)
            epsilon= [0] * len(line)
            
        for i, bit in enumerate(line):   
            gamma[i] = gamma[i] + int(bit)

    total_entries = index +1


    for index, gammebit in enumerate(gamma):
        gamma[index] = "0" if gammebit < (total_entries/2) else "1"
        

    gammareading = ["".join(d for d in gamma)]
    return gammareading


def get_items_with_mostprominent_bit(inputList,bitindex,mostprominent_bit):
    outputList=[]
    inputListSize = 0
    for item in inputList:
        inputListSize = inputListSize +1
        if int(item[bitindex]) == mostprominent_bit:
            
            outputList.append(item)
        
    if inputListSize == 1:
        return inputList
    return outputList

def find_mostprominent(inputList,bitindex, prominence):
    itemSum = 0
    count = 0
    for item in inputList:
        itemSum = itemSum + int(item[bitindex])
        
        count = count +1
    
    if prominence:
        return 1 if itemSum >= (count/2) else 0
    return 0 if itemSum >= (count/2) else 1

def calculate_rating(gamma,rating):
    prominance = True
    if rating == "co2":
        prominance = False
    mostprominent_bit = find_mostprominent(filereader("day3binput"),0,prominance)
    itemsWithMostprominentBits = get_items_with_mostprominent_bit(filereader("day3binput"),0,mostprominent_bit)
    for bitindex in range(len(gamma[0])):
        if bitindex == 0:
            continue
        mostprominent_bit = find_mostprominent(itemsWithMostprominentBits,bitindex,prominance)
        
        itemsWithMostprominentBits = get_items_with_mostprominent_bit(itemsWithMostprominentBits,bitindex,mostprominent_bit)
    return list(set(itemsWithMostprominentBits))
        

if __name__ == "__main__":
    gamma = getGamma()
    oxygen =calculate_rating(gamma,"oxygen")
    co2 =calculate_rating(gamma,"co2")
    gammaInt =int(gamma[0],2) 
    oxygenInt =int(oxygen[0],2) 
    co2Int =int(co2[0],2) 
    LifeSupportRating = oxygenInt * co2Int
    print(f"{gammaInt=}")
    print(f"{co2Int=}")
    print(f"{oxygenInt=}")
    print(f"{LifeSupportRating=}")
    # print(f"{output=}")



