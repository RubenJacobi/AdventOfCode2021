inputsize = -1
def filereader(filename):
    for line in open(filename, "r"):
        yield line.rstrip()


def findsomething(item, list1):
    if item in (list1):
        return item
    return None


epsilon= None
oxygen = []
co2 = []
ListOfLists= []
Gdstlist=[]
Edstlist = []
bufferList = []
bufferList2 = []
epsilonCalc = None

def getGamma():
    gamma = None
    for index, line in enumerate(filereader("day3a_testinput")):
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


def getEpsilon(diagnostics_report,index):
    epsiolon = None
    for diagnostic in diagnostics_report:
        if epsiolon == None:
            epsiolon= [0] * len(diagnostic)
            
        for i, bit in enumerate(diagnostic):   
            epsiolon[i] = epsiolon[i] + int(bit)
            
    for index, gammebit in enumerate(epsiolon):
        epsiolon[index] = "0" if gammebit < (len(diagnostics_report)/2) else "1"
        
    if index != len(diagnostics_report[0]):
        getEpsilon(diagnostics_report,index)
    else:
        global epsilonCalc
        epsilonCalc = diagnostics_report
    
    
print(f"{getGamma()=}")

# for line in filereader("day3a_testinput"):
    
#     if line[0] == gammareading[0][0]:
#         ListOfLists.append(line)
    
    

        
# def repeat(listt):
#     for i in range(1,len(gamma)):
#         for item in listt:
#             print(f"{item=}")
#             for i, bit in enumerate(item):   
#                 epsilon[i] = epsilon[i] + int(bit)
#     return 

# for index, gammebit in enumerate(gamma):
#     gamma[index] = "0" if gammebit < (total_entries/2) else "1"
    
#         if item[i] == epsilonreading[0][i]:
#             for index, gammebit in enumerate(Edstlist):
                
#                 epsilon[index] = "1" if float(gammebit) < (total_entries/2) else "0"
#         bufferList.append(item)       
#     Edstlist = list(bufferList)
#     print(f"{Edstlist=}")
    
    
# print(Gdstlist)
# print(Edstlist)
# gammareading = ["".join(d for d in gamma)]
# epsilonreading = ["".join(d for d in epsilon)]
# consumption = int(Gdstlist[0],2) * int(Edstlist[0],2)
# print(ListOfLists)
# print(consumption)