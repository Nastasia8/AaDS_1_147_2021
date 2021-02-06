
text = "Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects. Python is dynamically-typed and garbage-collected.".lower()
countP = 0
countO = 0
for letter in text:
    if letter=='p':
        countP+=1
    if letter == 'o':
        countO+=1
print(countP, countO)
 
    
