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

print("_"*10)

number= 62
while True:
    guess= int(input("Guess the number."))
    if guess < number:
        print("It is higher.")
    elif guess > number:
        print("It is lower.")
    else:
        print("That is right.")
        break