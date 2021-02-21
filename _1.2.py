from math import sqrt,pi
T=0
W=0

a= int(input())
b= int(input())

T = 2* pi * sqrt(a/b)
W=1/T

print("период колебаний пружинного маятника:",T,"циклическая частота:",W)

