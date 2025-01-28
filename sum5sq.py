#Prints the minimum number of terms required to express integers 1 <= j <= n as the sum of distinct squares, or 7 if it is not possible.
n = 983040
Clol = []
C = []
Clol.append(C.copy())
for j in range(n+1):
  C.append(7)
Clol.append(C.copy())
Clol[1][1] = 1
Clol[1][0] = 0
i = 2
i2 = i*i
while i2 <= n:
  del C
  C = []
  C.append(0)
  for j in range(1,n+1):
    if j < i*i:
      C.append(Clol[i-1][j])
    else:
      temp1 = 1+Clol[i-1][j-i2]
      temp2 = Clol[i-1][j]
      if temp1 > temp2:
        C.append(temp2)
      else:
        C.append(temp1)
  Clol[i-1] = 0
  Clol.append(C.copy())
  i+=1
  i2 = i*i
i-=1
for j in range(1,n+1):
  print(j, Clol[i][j])
