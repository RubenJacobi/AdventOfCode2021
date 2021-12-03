inputsize = -1
def filereader(filename):
    for line in open(filename, "r"):
        yield line.rstrip()


gamma = None
epsilon= [0,0,0,0,0]

for index, line in enumerate(filereader("day3ainput")):
    if gamma == None:
        gamma= [0] * len(line)
        epsilon= [0] * len(line)
    for i, bit in enumerate(line):   
        gamma[i] = gamma[i] + int(bit)

total_entries = index +1


for index, gammebit in enumerate(gamma):
    gamma[index] = "0" if gammebit < (total_entries/2) else "1"
    epsilon[index] = "1" if gammebit < (total_entries/2) else "0"
    
    
gammareading = ["".join(d for d in gamma)]
epsilonreading = ["".join(d for d in epsilon)]
consumption = int(gammareading[0],2) * int(epsilonreading[0],2)

print(consumption)