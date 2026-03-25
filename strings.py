curso = "Python"

print(curso.center(11, "*"))
print(" # ".join(curso))

nome = "Ardalto"
idade = 33
profissao = "Desenvolvedor"
linguagem = "Python"

print("nome: %s, idade: %d, profissão: %s, linguagem: %s" % (nome, idade, profissao, linguagem))

print("nome: {}, idade: {}, profissão: {}, linguagem: {}".format(nome, idade, profissao, linguagem))

print("nome: {0}, idade: {1}, profissão: {2}, linguagem: {3}".format(nome, idade, profissao, linguagem))

print(f"nome: {nome}, idade: {idade}, profissão: {profissao}, linguagem: {linguagem}")

#string tripla

nome = "Ardalto"

mensagem = f"""
Olá, meu nome é {nome},
Eu sou um desenvolvedor Python.
              Testando um novo conhecimento
                            Mas uma linha!
"""

print(mensagem)


curso = "Python"

print(curso[::-1])