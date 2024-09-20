with open("./input1b.txt", "r") as inputFileOpening: 
  inputFile = inputFileOpening.readlines() 

  
vertices = int(inputFile[0].split(" ")[0])

adjacencyList = [0]*(vertices+1)

for i in inputFile[1:]:
  elements = i.split(" ")  
  if adjacencyList[int(elements[0])] == 0:
    adjacencyList[int(elements[0])] = [(int(elements[1]), int(elements[2]))]
  else: 
    adjacencyList[int(elements[0])].append((int(elements[1]), int(elements[2])))

with open("output1b.txt", "a") as outputFile:
  for i in range(len(adjacencyList)):
    if adjacencyList[i] == 0:
      outputFile.writelines(f"{i} : ") 
    else: 
      outputFile.writelines(f"{i} : ") 
      for eachTuple in adjacencyList[i]: 
        outputFile.writelines(f"{eachTuple} ") 
    outputFile.writelines("\n")