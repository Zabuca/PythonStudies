'''
Em Python, uma tupla é uma estrutura de dados semelhante a uma lista, porém imutável. Isso significa que uma vez que uma tupla é criada, seus 
elementos não podem ser alterados, adicionados ou removidos. As tuplas são definidas utilizando parênteses `()` e os elementos são separados por vírgulas.

Aqui está um exemplo simples de como criar e usar uma tupla em Python:

```python
# Criando uma tupla
tupla = (10, 20, 30, 40, 50)

# Acessando elementos da tupla por índice
print(tupla[0])  # Saída: 10
print(tupla[1])  # Saída: 20

# Tentativa de alterar um elemento da tupla (isso resultará em um erro)
tupla[1] = 25  # TypeError: 'tuple' object does not support item assignment

# Iterando sobre os elementos da tupla
for elemento in tupla:
    print(elemento)

# Obtendo o comprimento da tupla
print(len(tupla))  # Saída: 5
```

Aqui estão alguns dos métodos mais comuns e operações que podem ser realizadas com tuplas:

- Acessar elementos por índice: Assim como em listas, você pode acessar os elementos de uma tupla utilizando a indexação.
- Iteração: Você pode iterar sobre os elementos de uma tupla usando loops `for`.
- Comprimento: Você pode usar a função `len()` para obter o comprimento (número de elementos) de uma tupla.
- Concatenação: Você pode concatenar duas tuplas utilizando o operador `+`.
- Repetição: Você pode repetir os elementos de uma tupla utilizando o operador `*`.
- Verificação de existência: Você pode verificar se um elemento está presente em uma tupla utilizando o operador `in`.

Aqui está um exemplo de uso dessas operações com tuplas:

```python
# Criando duas tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

# Concatenando as duas tuplas
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)  # Saída: (1, 2, 3, 4, 5, 6)

# Repetindo os elementos de uma tupla
tupla_repetida = tupla1 * 3
print(tupla_repetida)  # Saída: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Verificando a existência de um elemento em uma tupla
print(2 in tupla1)  # Saída: True
print(7 in tupla2)  # Saída: False
```

As tuplas são úteis quando você precisa de uma coleção de elementos que não devem ser alterados durante a execução do programa, como por 
exemplo coordenadas geográficas, informações de um ponto em um gráfico, entre outros. Elas também podem ser mais eficientes em termos de 
memória e processamento do que listas em algumas situações, devido à sua imutabilidade.
'''
