a = [[1,2,3],
     [4,5,6],
     [7,8,9]]

def print_massive(arr):
    for i in range(len(arr)):
      for j in range(len(arr[i])):
        print(arr[i][j] , end= "\t")
      print()

print_massive(a)

