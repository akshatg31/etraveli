def tpose(arr,transposed):
    for i in range(N):
      for j in range(N):
        transposed[i][j]=arr[j][i]

arr = [ [1,5,7],
        [6,5,8],
        [4,3,9]]
N=len(arr)
 
transposed = arr[:][:]
 
tpose(arr, transposed)
 
print("Transposed is ")
for i in range(N):
    for j in range(N):
       print(transposed[i][j], " ", end='')
    print()
