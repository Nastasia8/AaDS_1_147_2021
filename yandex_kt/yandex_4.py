def main():
    N = int(input())
    mass = list(map(int, input().split(" ")))
    mass, result = sort(mass)
    print(result)

def sort(mass):
    n = len(mass)
    if n <= 1:
        return(mass, 0)
    half = n//2
    A, left = sort(mass[:half])    
    B, right = sort(mass[half:])
    res, inver = merge(A, B)
    return(res, inver + left + right)
    
def merge(A, B):
    res = []
    inver = i = j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            res.append(A[i])
            i += 1
        else:
            res.append(B[j])
            j += 1
            inver += len(A) - i
    while i < len(A):
        res.append(A[i])
        i += 1
    while j < len(B):
        res.append(B[j])
        j += 1
    return(res, inver)    

main()
