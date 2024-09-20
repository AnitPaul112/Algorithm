with open("input1a.txt",'r') as file :
    next(file)
    with open("output1a.txt","w") as file2:
        for line in file:
            file2.write(line)
            line=line.strip()
            if int(line)%2!=0:
                print(line,"is odd number")
            else:
                print(line,'is even number')