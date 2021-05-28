#sort 1
N = int(input())
numbers = [int(i) for i in input().split()][:N]

check = 0

for i in range(N-1):
    for j in range(N-i-1):
	    if numbers[j] > numbers[j+1]:
		    numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
		    print(" ".join(map(str, numbers)))
		    check = 1
    
if check == 0:
	print(0)
	
#sort 2
N = int(input())
a = []

for i in range(N):
    a.append([int(j) for j in input().split()][:N])

for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j+1][1] > a[j][1]:
            a[j+1],a[j] = a[j],a[j+1]

for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j+1][1] == a[j][1]:
            if a[j+1][0] < a[j][0]:
                a[j+1],a[j] = a[j],a[j+1]

for i in range(len(a)):
    print(*a[i])

#sort 3
  
def main():
    n = int(input())
    a = list(map(int,input().split()))[:n]
    merge(a,0,len(a))
    print(*a,sep=" ")
def merge(a,start,end):
    if end - start > 1:
        middle = (start + end)//2
        merge(a,start,middle)
        merge(a,middle,end)
        left = a[start:middle]
        right = a[middle:end]
        internal_sort(a,left,right,start)
        print(start+1,end,a[start],a[end-1])
def internal_sort(arr,left,right,start):
    j = i = 0
    k = start
    while i<len(right) and j<len(left):
        if left[j] > right[i]:
            arr[k] = right[i]
            i+=1
        else:
            arr[k] = left[j]
            j+=1
        k+=1
    while j<len(left):
        arr[k] = left[j]
        j+=1
        k+=1
    while i<len(right):
        arr[k] = right[i]
        i+=1
        k+=1
main()

#sort 4

def count_inversions(a):
  res = 0
  counts = [0]*(len(a)+1)
  rank = { v : i+1 for i, v in enumerate(sorted(a)) }
  for x in reversed(a):
    i = rank[x] - 1
    while i:
      res += counts[i]
      i -= i & -i
    i = rank[x]
    while i <= len(a):
      counts[i] += 1
      i += i & -i
  return res

N = int(input())
numbers = [int(i) for i in input().split()][:N]

print(count_inversions(numbers))

#sort 5

N = int(input())

numbers = [int(i) for i in input().split()][:N]

print(len(set(numbers)))

