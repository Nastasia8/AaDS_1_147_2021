p=0
o=0
for i in 'Python is an interpreted, high-level and general-purpose programming language. Pythons design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects. Python is dynamically-typed and garbage-collected.'.lower():
    if i == "p":
        p += 1
    if i == "o":
        o += 1
print ("p=",p,"o=",o)
