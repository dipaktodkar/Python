x=2
print(x)
y=float(x) #changed data type from integer to float
print(y)
z=int(y) #changed data type from float to integer
print(z)
a=123
b="123"
c=str(a) #changed data type from integer to string
d=int(b) #changed data type from string to integer
print(c), print(type(c))
print(f"Is c of string type ? {isinstance(c, str)}")
print(d), print(type(d))
print(f"Is d of string type ? {isinstance(d, str)}")
