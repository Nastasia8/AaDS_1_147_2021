text = "Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects. Python is dynamically-typed and garbage-collected." 
p = 0
o = 0

for letter in text.lower():
    if letter == "p":
        p += 1
    elif letter == "o":
        o += 1
    
print(o,p)