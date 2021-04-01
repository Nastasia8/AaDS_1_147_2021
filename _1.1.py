a= "Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects. Python is dynamically-typed and garbage-collected."
o=0
p=0

for i  in a:
	if i == "o":
		o+=1

for i  in a:
	if i == "p":
		p+=1

print ("количество o:", o,"количество p:",p)
