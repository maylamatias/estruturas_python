name = input("Qual é o seu nome ?")
age = input("Qual é a sua idade ?")

print(type(name))
print(type(age))


age = int(age)

older = age + 10

print(f"{name} terá {older} daqui a 10 anos.")