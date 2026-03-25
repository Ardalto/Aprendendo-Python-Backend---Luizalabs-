nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

print(f"Olá {nome}, você tem {idade} anos.");
print(nome, idade);
print(nome, idade, end="...\n");
print(nome, idade, sep="#", end="...\\n");
print(nome, idade, sep="#", end="...\\n", flush=True);
print(nome, idade, sep="#")