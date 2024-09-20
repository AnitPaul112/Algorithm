input=open("input3.txt","r")
output=open("output3.txt","w")
k=int(input.readline())
l1=[]
for i in range(k):
  a=input.readline()
  b=a.split(" ")
  c=(int(b[0]),int(b[1]))
  l1.append(c)


for i in range(len(l1)-1):
  for j in range(i+1,len(l1)):
    p=l1[i]
    q=l1[j]
    if q[1]<p[1]:
      l1[i],l1[j]=l1[j],l1[i]

new=[]
m=0
st=0
et=0
for i in l1:
  a=i[0]
  b=i[1]
  if a>=et:
    st=a
    et=b
    m+=1
    new.append(i)
output.write(f"{str(m)}\n")
for i in new:
  output.write(f"{str(i)} \n")