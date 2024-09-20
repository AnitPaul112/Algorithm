with open('input1b.txt','r') as file:
    with open('output1b.txt','w') as file2:
        next(file) 
        for line in file:
            arr=line.split()
            print(arr)
            if arr[2]=="+":
                result=(int(arr[1])+int(arr[3]))
            if arr[2]=="-":
                result=(int(arr[1])-int(arr[3]))
            if arr[2]=="*":
                result=(int(arr[1])*int(arr[3]))
            if arr[2]=="/":
                result=(int(arr[1])/int(arr[3]))
            file2.write(f'The result of {arr[1]} {arr[2]} {arr[3]} is {result} \n')
        