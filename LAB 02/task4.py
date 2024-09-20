infile=open('input4.txt','r')
outfile=open('output4.txt','w')
n,p=tuple(map(int,infile.readline().split()))
l=[]
l1=[0]*p
count=0
for i in range(n):
  a=infile.readline()
  tup=tuple(map(int,a.split()))
  l.append(tup)
for i in range(n):
  for j in range(n-i-1):
    if l[j][1]>l[j+1][1]:
      l[j],l[j+1]=l[j+1],l[j]

for i in l:
  start_time,end_time=i[0],i[1]
  for j in range(p):
    if l1[j]<=start_time:
      l1[j]=end_time
      count+=1
      break
outfile.write(str(count))



infile.close()
outfile.close()