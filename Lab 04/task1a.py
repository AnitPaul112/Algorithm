with open("./input1a.txt", "r") as inputFileOpening: 
  inputFile = inputFileOpening.readlines() 


vertices = int(inputFile[0].split(" ")[0])

adjacencyMatrix = []      
for i in range(vertices + 1):
  l = [0]*(vertices + 1)  
  adjacencyMatrix.append(l)

for i in inputFile[1:]:
  elements = i.split(" ")   
  adjacencyMatrix[int(elements[0])][int(elements[1])] = int(elements[2])


with open("output1a.txt", "a") as outputFile:
  for i in range(len(adjacencyMatrix)): 
    for j in range(len(adjacencyMatrix[i])): 
      outputFile.writelines(f"{adjacencyMatrix[i][j]} ")
    outputFile.writelines("\n")