'''
Em Python, um conjunto (set) é uma estrutura de dados que representa uma coleção não ordenada e mutável de elementos únicos. 
Assim como na teoria de conjuntos da matemática, um conjunto em Python não permite elementos 
duplicados e não mantém uma ordem específica para os elementos.

A similaridade entre conjuntos em Python e conjuntos na matemática é bastante forte. Aqui estão algumas semelhanças importantes:

1. **Elementos Únicos:** Tanto em Python quanto na matemática, um conjunto é uma coleção de elementos distintos, onde cada elemento 
aparece apenas uma vez. Isso significa que não há repetição de elementos em um conjunto.

2. **Operações de Conjunto:** Assim como na matemática, em Python você pode realizar várias operações de conjunto com conjuntos, como 
união, interseção, diferença e complemento. Essas operações são fundamentais para manipular conjuntos e realizar análises conjunturais.

3. **Notação:** A notação usada em Python para representar conjuntos é semelhante à usada na matemática. Em Python, um conjunto é 
definido utilizando chaves `{}` e os elementos são separados por vírgulas. Na matemática, conjuntos são representados entre chaves 
também, e os elementos são listados separados por vírgulas.

4. **Eficiência de Operações:** Tanto em Python quanto na matemática, as operações de conjunto são eficientes e fornecem maneiras 
poderosas de manipular conjuntos de elementos. Em Python, as operações de conjunto são implementadas de forma otimizada, permitindo
que você realize essas operações de forma rápida e eficiente.

No geral, conjuntos em Python são uma implementação prática e eficiente da teoria de conjuntos da matemática, permitindo que você 
trabalhe com coleções de elementos únicos de forma simples e eficaz. Eles são amplamente utilizados em Python para uma variedade de  
tarefas, como remoção de duplicatas, verificação de pertencimento, entre outras operações conjunturais.

Claro! Vou fornecer exemplos que ilustram cada ponto mencionado:

### 1. Elementos Únicos:
Em Python, os conjuntos não permitem elementos duplicados. Se você tentar adicionar um elemento que já está presente no conjunto, ele 
será ignorado.

```python
# Criando um conjunto com elementos únicos
conjunto = {1, 2, 3, 4, 5, 1, 2}
print(conjunto)  # Saída: {1, 2, 3, 4, 5}
```

### 2. Operações de Conjunto:
Python fornece operações de conjunto nativas para realizar união, interseção, diferença e outras operações.

```python
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

# União de conjuntos
uniao = conjunto1.union(conjunto2)
print(uniao)  # Saída: {1, 2, 3, 4, 5}

# Interseção de conjuntos
intersecao = conjunto1.intersection(conjunto2)
print(intersecao)  # Saída: {3}

# Diferença de conjuntos
diferenca = conjunto1.difference(conjunto2)
print(diferenca)  # Saída: {1, 2}
```

### 3. Notação:
A notação para conjuntos em Python é semelhante à usada na matemática. Os elementos são listados entre chaves `{}` e separados por 
vírgulas.

```python
# Criando um conjunto em Python
conjunto_python = {1, 2, 3, 4, 5}
print(conjunto_python)  # Saída: {1, 2, 3, 4, 5}
```

### 4. Eficiência de Operações:
As operações de conjunto em Python são eficientes e otimizadas para lidar com grandes conjuntos de elementos.

```python
# Criando conjuntos grandes para demonstração
conjunto_grande1 = set(range(100000))
conjunto_grande2 = set(range(50000, 150000))

# Realizando operações de conjunto
uniao = conjunto_grande1.union(conjunto_grande2)
intersecao = conjunto_grande1.intersection(conjunto_grande2)
diferenca = conjunto_grande1.difference(conjunto_grande2)

# Imprimindo tamanhos dos conjuntos resultantes
print(len(uniao))  # Saída: 150000
print(len(intersecao))  # Saída: 50000
print(len(diferenca))  # Saída: 50000
```

Esses exemplos demonstram como conjuntos em Python funcionam de forma semelhante à teoria de conjuntos da matemática, fornecendo uma
maneira eficiente de trabalhar com coleções de elementos únicos.
'''

print('Hello world')