print("print vs. f string:")
print("")

print("My name is Arman and I'm 20 years old.")
print("-"*10)
name= "Arman"
age= 20
print(f"My name is {name} and I am {age} years old.")

print("_"*10)

print("\nWhile loop vs. For loop:")
print("")

i = 0
while i < 10:
    print(i)
    i += 1
print("-"*10)
for j in range(10):
    print(j)