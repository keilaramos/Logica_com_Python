# As variáveis têm outras propriedades além de nomes e valores.
# Uma delas é o tipo e define a natureza dos dados que a variável armazena.

# Tipos de variáveis em Python
# Inteiro (int)
# Ponto Flutuante ou Decimal (float)
# Tipo Complexo (complex)
# String (str)
# Boolean (bool)- tipo lógico (True/False)
# List (list)
# Tuple.
# Dictionary (dic)

# Variáveis tipo numéricas (int, float)

a = 14
b = 14.0
tipo_a = type(a)
tipo_b = type(b)

# Variáveis tipo lógico (True/False)

resultado = True
tipo_resultado = type(resultado)

# operadores relacionais
# == igualdade
# > maior que 
# < menor que 
# != diferente
# >= maior ou igual
# <= menor ou igual

# # Operadores lógicos
# not --> não 
# and --> e
# or --> ou 

# tabela verdade and  / or 
# V    V      =   V  /  V
# V    F      =   F  /  V
# F    V      =   F  /  V
# F    F      =   F  /  F   


# Variável Tipo String (str)
# As strings armazenam cadeias de caracteres.
# o tamanho de uma string pode ser obtido usando a função len().
# Retorna o Nº de caracteres na string.

c = "123"
tipo_c = type(c)
d = "14"
tipo_d = type(d)

#Printando cada tipo

print(tipo_a, tipo_b, tipo_resultado, tipo_c, tipo_d, len(c))

# Operações 
# - concatenação(+)
print(c + d)

# - composição (%d, %s, %f) -marcadores de posições.
nome = "João"
idade = 22
grana = 51.36
print("%s tem %d anos e R$%f no bolso" % (nome, idade, grana))

# - método format em vez de %
print("{} tem {} anos e R${} no bolso" .format(nome, idade, grana))
print("{:12} tem {:03} anos e R${:5.2f} no bolso" .format(nome, idade, grana))
print(f"{nome} tem {idade} anos e R${grana:5.2f} no bolso")

# - fatiamento
print(nome[0:3])


