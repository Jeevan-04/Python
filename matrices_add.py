x=[[2,5,4],
   [1,3,9],
   [7,6,2]]
y=[[1,8,5],
   [7,3,6],
   [4,0,9]]
k=[[0,0,0],[0,0,0],[0,0,0]]
'''for i in range(3):
    for j in range(3):
        k[i][j]=x[i][j]+y[i][j]
    print(k[i])'''

k=[]
for i in range(3):
    for j in range(3):
        k.append(x[i][j]+y[i][j])