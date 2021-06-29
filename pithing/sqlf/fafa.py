import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-SV75JJT;'
                      'Database=testbase;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM dbo.eugdpgrowth')
arr=[]
for row in cursor:
    arr.append(row)

print(arr.__len__())

firsty=[]
firstx=[]
secondy=[]
secondx=[]
thirdy=[]
thirdx=[]
fourthy=[]
fourthx=[]
fifthy=[]
fifthx=[]
i=1
j=0
x=[]
graph1=[]
while j<arr.__len__():
    firsty.append(arr[j][0])
    print(firsty[j]) 
    while i<arr[0].__len__():
        graph1.append(arr[j][i])
        i=i+1
    i=1
    j=j+1
print(graph1)

cursor.execute('SELECT * FROM dbo.pharmacy')
arr1=[]
for row in cursor:
    arr1.append(row)
print(arr1)
i=1
j=0
graph2=[]
while j<arr1.__len__():
    secondy.append(arr1[j][0])
    print(secondy[j]) 
    while i<arr1[0].__len__():
        graph2.append(float(arr1[j][i]))
        i=i+1
    i=1
    j=j+1
cursor.execute('SELECT * FROM dbo.local')
arr2=[]
for row in cursor:
    arr2.append(row)
print(arr2)
i=1
j=0
graph3=[]
while j<arr2.__len__():
    thirdy.append(arr2[j][0])
    print(thirdy[j]) 
    while i<arr2[0].__len__():
        graph3.append(float(arr2[j][i]))
        i=i+1
    i=1
    j=j+1
cursor.execute('SELECT * FROM dbo.usgdp')
arr3=[]
for row in cursor:
    arr3.append(row)
print(arr3)
i=1
j=0
graph4=[]
while j<arr3.__len__():
    fourthy.append(arr3[j][0])
    print(thirdy[j]) 
    while i<arr3[0].__len__():
        graph4.append(float(arr3[j][i]))
        i=i+1
    i=1
    j=j+1
cursor.execute('SELECT * FROM dbo.usun')
arr4=[]
for row in cursor:
    arr4.append(row)
print(arr4)
i=1
j=0
graph5=[]
while j<arr4.__len__():
    fifthy.append(arr4[j][0])
    print(thirdy[j]) 
    while i<arr4[0].__len__():
        graph5.append(float(arr4[j][i]))
        i=i+1
    i=1
    j=j+1
###while i<arr.__len__():
###    secondy.append(arr[1][i])
###    i=i+1
###i=0
###while i<arr.__len__():
###    thirdy.append(arr[2][i])
###    i=i+1
###i=0
###while i<arr.__len__():
###    fourthy.append(arr[3][i])
###    i=i+1


###print(firsty[3])
###print(secondy[3])
###print(thirdy[3])
###print(fourthy[3])