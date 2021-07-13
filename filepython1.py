file=open('C:/Users/Roshan Dafal/Desktop/Python/sample.log')
x=file.readlines()
count=0
l=[]
for i in x:
   if 'rules violated'in i:
       l.append(i)
for i in l:
    count=count+int(i[1:len(i)-15])
print(count)           