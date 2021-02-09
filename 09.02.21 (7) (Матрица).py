m=[[1,2],[3,4]]
print(*[m[i][-i-1] for i in range(len(m))],sep='\n')
