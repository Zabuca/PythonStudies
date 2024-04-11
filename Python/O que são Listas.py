'''
Em Python, uma lista é uma estrutura de dados que permite armazenar uma coleção ordenada de itens. Esses itens podem ser de qualquer tipo,
como números, strings, booleanos, outras listas e até mesmo objetos mais complexos. As listas são mutáveis, o que 
significa que você pode modificar, adicionar e remover itens conforme necessário.

Aqui está um exemplo simples de como criar e usar uma lista em Python:

#```python
# Criando uma lista vazia
minha_lista = []

# Adicionando elementos à lista usando o método append()
minha_lista.append(10)
minha_lista.append(20)
minha_lista.append(30)

# Acessando elementos da lista por índice
print(minha_lista[0])  # Saída: 10
print(minha_lista[1])  # Saída: 20
print(minha_lista[2])  # Saída: 30

# Alterando elementos da lista
minha_lista[1] = 25

# Removendo elementos da lista usando o método remove()
minha_lista.remove(10)

# Imprimindo a lista atualizada
print(minha_lista)  # Saída: [25, 30]
```

Aqui estão alguns dos comandos mais usados com listas em Python:

- `append(item)`: Adiciona um item ao final da lista.
- `insert(index, item)`: Insere um item em uma posição específica na lista.
- `remove(item)`: Remove o primeiro item da lista que corresponde ao valor fornecido.
- `pop([index])`: Remove e retorna o item na posição especificada (ou o último item se nenhum índice for fornecido).
- `index(item)`: Retorna o índice da primeira ocorrência do item na lista.
- `count(item)`: Retorna o número de ocorrências do item na lista.
- `sort()`: Classifica os itens da lista em ordem crescente.
- `reverse()`: Inverte a ordem dos itens na lista.

Agora, vejamos como usar alguns desses comandos:

'python
# Criando uma lista
lista = [10, 20, 30, 40]

# Adicionando um item ao final da lista
lista.append(50)

# Inserindo um item em uma posição específica
lista.insert(2, 25)

# Removendo um item da lista
lista.remove(20)

# Removendo e retornando o último item da lista
ultimo_item = lista.pop()

# Encontrando o índice de um item na lista
indice = lista.index(30)

# Contando o número de ocorrências de um item na lista
ocorrencias = lista.count(25)

# Classificando os itens da lista
lista.sort()

# Invertendo a ordem dos itens na lista
lista.reverse()

print(lista)  # Saída: [40, 30, 25, 10]
print(ultimo_item)  # Saída: 50
print(indice)  # Saída: 1
print(ocorrencias)  # Saída: 1
``` 

Esses são apenas alguns dos comandos mais comuns para usar e para manipular listas em Python. Com eles, você pode realizar 
uma variedade de operações úteis em suas listas, desde adicionar e remover itens até ordená-los e manipular sua estrutura.

O método `.pop()` em Python é usado para remover e retornar o último elemento de uma lista, ou remover e retornar um 
elemento em uma posição específica, se um índice for fornecido como argumento.

Aqui está a sintaxe do método `.pop()`:

```python
elemento_removido = lista.pop([índice])
```

- `lista`: A lista da qual você deseja remover o elemento.
- `[índice]` (opcional): O índice do elemento que você deseja remover. Se nenhum índice for fornecido, o método `.pop()` 
removerá e retornará o último elemento da lista.

O método `.pop()` modifica a lista original, removendo o elemento selecionado. Se você fornecer um índice, o método 
retornará o elemento removido. Se nenhum índice for fornecido, ele simplesmente removerá o último elemento e não retornará nada.

Aqui está um exemplo de uso do método `.pop()`:

```python
lista = [10, 20, 30, 40, 50]

# Removendo e retornando o último elemento da lista
ultimo_elemento = lista.pop()
print(ultimo_elemento)  # Saída: 50
print(lista)  # Saída: [10, 20, 30, 40]

# Removendo e retornando o elemento na posição 2 da lista
elemento_removido = lista.pop(2)
print(elemento_removido)  # Saída: 30
print(lista)  # Saída: [10, 20, 40]
```

No primeiro exemplo, o método `.pop()` é usado sem um índice, então ele remove e retorna o último elemento da lista, que é 50. 
No segundo exemplo, o método `.pop(2)` remove e retorna o elemento na posição 2 da lista, que é 30. Após cada chamada do método
`.pop()`, a lista é modificada para refletir a remoção do elemento selecionado.

P



Para somar os itens de uma lista em Python, você pode usar a função `sum()` que soma todos os elementos da lista e retorna o resultado. 
Aqui está um exemplo de como fazer isso:

```python
lista = [10, 20, 30, 40, 50]
soma = sum(lista)
print(soma)  # Saída: 150
```

Neste exemplo, a função `sum()` é usada para somar todos os elementos da lista `lista`, que contém os números de 10 a 50. O resultado, 
que é a soma de todos esses números, é então armazenado na variável `soma` e impresso na tela.

Você também pode somar os itens de uma lista de maneira mais explícita usando um loop. Aqui está um exemplo usando um loop `for`:

```python
lista = [10, 20, 30, 40, 50]
soma = 0
for elemento in lista:
    soma += elemento
print(soma)  # Saída: 150
```

# Neste exemplo, inicializamos a variável `soma` com 0 e, em seguida, iteramos sobre cada elemento na lista, adicionando o valor do elemento 
# à variável `soma` em cada iteração. Isso resulta na soma de todos os elementos da lista.
'''
'''
Para somar apenas os três primeiros itens de uma lista em Python, você pode usar a indexação da lista para selecionar os três primeiros 
elementos e, em seguida, somá-los. Aqui está como fazer isso:

```python
lista = [10, 20, 30, 40, 50]
soma_primeiros_tres = sum(lista[:3])
print(soma_primeiros_tres)  # Saída: 60
'''
'''
Neste exemplo, `lista[:3]` retorna uma sublista contendo os três primeiros elementos da lista `lista`. Então, a função `sum()` é usada para somar 
os elementos desta sublista, resultando na soma dos três primeiros itens da lista original.

Usar a sintaxe `lista[inicio:fim]` permite que você selecione uma porção específica da lista, indo do índice `inicio` (inclusive) até o índice `fim` 
(exclusivo). Se `inicio` não for fornecido, ele começa do início da lista. Se `fim` não for fornecido, ele vai até o final da lista.

Neste caso, `lista[:3]` seleciona os elementos da lista do índice 0 até o índice 2, que são os três primeiros elementos. Em seguida, `sum(lista[:3])` 
soma esses elementos selecionados.

'''
'''
Para mostrar cada índice da lista em uma linha separada, você pode iterar sobre a lista e imprimir cada elemento individualmente. Aqui está como fazer 
isso em Python:

```python
lista = [10, 20, 30, 40, 50]

# Iterando sobre a lista e imprimindo cada elemento em uma linha separada
for indice, valor in enumerate(lista):
    print(f"Índice {indice}: {valor}")
```

O resultado será:

```
Índice 0: 10
Índice 1: 20
Índice 2: 30
Índice 3: 40
Índice 4: 50
```

Neste exemplo, `enumerate(lista)` retorna um iterador que fornece tanto o índice quanto o valor para cada elemento na lista. Usando um loop `for`, podemos
iterar sobre esses pares índice-valor e imprimir cada um em uma linha separada. A f-string (format string) é usada para formatar a saída, mostrando o índice e o valor de cada elemento da lista.

'''